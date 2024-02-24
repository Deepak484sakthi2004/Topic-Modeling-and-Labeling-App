#framework
import streamlit as st
# for topic modelling libraries
import gensim
from gensim import corpora, models
import re
import shutil
import os
# for labelling 
import heapq # it is a priority queue (min heap) returns the min when poll it(java)
import labels as lb # user-defined labelling python file
# for CSV
import pandas as pd
# for Video
import whisper
from pytube import YouTube
from pathlib import Path

# FUNCTIONS

# function for text preprocessing(tokens, stoi,itos) anol
def preprocess_text(text):
    # Replace this with your own preprocessing code
    # This example simply tokenizes the text and removes stop words
    tokens = gensim.utils.simple_preprocess(text)
    stop_words = gensim.parsing.preprocessing.STOPWORDS
    preprocessed_text = [[token for token in tokens if token not in stop_words]]

    return preprocessed_text
# Topic Modelling funcion(LDA-Latent Dirichlet Allocation)
def perform_topic_modeling(transcipt_text , num_topics = 5 , num_words = 10):
    preprocessed_text = preprocess_text(transcipt_text) # get the tokenisation of 
                                                        #words from the input_text
    dictionary = corpora.Dictionary(preprocessed_text)
    # uploading the dictionary into the bag of words
    corpus = [dictionary.doc2bow(text) for text in preprocessed_text]

    lda_model = models.LdaModel(corpus = corpus , id2word = dictionary 
                                   , num_topics = num_topics)      
    
    # extract the most probable word from each topic
    topics = []
    for idx , topic in lda_model.print_topics(-1,num_words = num_words):
        # Extract the top words for each topic and store in a list
        topic_words = [word.split('*')[1].replace('"', '').strip() for word in topic.split('+')]
        topics.append((f"Topic {idx}", topic_words))

    return topics

# Functions for Labeling

def label_topic(text):
    #Given a piece of text, this function returns the top two industry labels that best match the topics discussed in the text.
    # Count the number of occurrences of each keyword in the text for each industry
    counts = {}
    for industry, keywords in lb.industries.items():
        count = sum([1 for keyword in keywords if re.search(r"\b{}\b".format(keyword), text, re.IGNORECASE)])
        counts[industry] = count
    # Get the top two industries based on their counts
    top_industries = heapq.nlargest(2, counts, key=counts.get) 
    
    # If only one industry was found, return it
    if len(top_industries) == 1:
        return top_industries[0]
    # If two industries were found, return them both
    else:
        return top_industries


# Functions to get audio and from video and text from audio

 # cache the resources of the model, so it doesnot runs for every reload
@st.cache_resource 
def load_model():
    model = whisper.load_model("base")
    return model

def save_video(url, video_filename):
    youtubeObject = YouTube(url)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")
    
    return video_filename

def save_audio(url):
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download()
    base, ext = os.path.splitext(out_file)
    file_name = base + '.mp3'
    try:
        os.rename(out_file, file_name)
    except WindowsError:
        os.remove(file_name)
        os.rename(out_file, file_name)
    audio_filename = Path(file_name).stem+'.mp3'
    video_filename = save_video(url, Path(file_name).stem+'.mp4')
    print(yt.title + " Has been successfully downloaded")
    return yt.title, audio_filename, video_filename

def audio_to_transcript(audio_file):
    model = load_model()
    result = model.transcribe(audio_file)
    transcript = result["text"]
    return transcript



# streamlit code
st.set_page_config(layout="wide")
choice = st.sidebar.selectbox("Select the type of file to upload",["Text","Video","CSV"])
st.title("Topic Modelling and Labeling App")

if choice=="Text":
    st.subheader("Topic Modelling and Labeling on Text file")
    input_text = st.text_area("Enter the input text",height=400)

    if input_text is not None:
        if st.button("Analyse Text"):
            col1,col2,col3  = st.columns([1,1,1]) # input data, topic modelling, labelling
            # topic modelling is
        # Topic modeling is a popular natural language processing technique
        #  used to create structured data from a collection of unstructured data
        # the technique enables businesses to learn the hidden semantic patterns
        #  portrayed by a text corpus and automatically identify the topics that 
        # exist inside it.

            with col1:
                st.info("Text is below")
                st.success(input_text)
            with col2:
                st.info("Text Modelling")
                topics = perform_topic_modeling(input_text)
                for topic in topics:
                    st.success(f"{topic[0]} : {', '.join(topic[1])}")
            with col3:
                st.info("Topic Labeling")
                labeling_text = input_text
                industry = label_topic(labeling_text)
                st.markdown("**Topic Labeling Industry Wise**")
                st.write(industry)

elif choice=="CSV":
    st.subheader("Topic Modelling and Labeling on CSV file")
    upload_csv = st.file_uploader("Upload the CSV",type=["csv"])
    if upload_csv is not None:
        if st.button("Analyse CSV"):
            col1,col2 = st.columns([1,1])
            with col1:
                st.info("CSV file")
                csv_file = upload_csv.name
                with open(os.path.join(csv_file),'wb') as f:
                    f.write(upload_csv.getbuffer())
                print(csv_file)
                df = pd.read_csv(csv_file,encoding = 'unicode-escape')
                st.dataframe(df)
            with col2:
                data_list = df['Data'].tolist()
                industry_list = []
                for i in data_list:
                    industry = label_topic(i)
                    industry_list.append(industry)
                df['Industry'] = industry_list
                st.info("Topic Modeling and Labeling")
                st.dataframe(df)




elif choice=="Video":
    st.subheader("Topic Modelling and Labeling on Video file")

