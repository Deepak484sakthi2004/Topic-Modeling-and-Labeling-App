
# use some of the labels to identify the the topics 
#### topic labeling ##########
insurance_keywords = ['actuary', 'claims', 'coverage', 'deductible', 'policyholder', 'premium', 'underwriter', 'risk assessment', 'insurable interest', 'loss ratio', 'reinsurance', 'actuarial tables', 'property damage', 'liability', 'flood insurance', 'term life insurance', 'whole life insurance', 'health insurance', 'auto insurance', 'homeowners insurance', 'marine insurance', 'crop insurance', 'catastrophe insurance', 'umbrella insurance', 'pet insurance', 'travel insurance', 'professional liability insurance', 'disability insurance', 'long-term care insurance', 'annuity', 'pension plan', 'group insurance', 'insurtech', 'insured', 'insurer', 'subrogation', 'adjuster', 'third-party administrator', 'excess and surplus lines', 'captives', 'workers compensation', 'insurance fraud', 'health savings account', 'health maintenance organization', 'preferred provider organization']

finance_keywords = ['asset', 'liability', 'equity', 'capital', 'portfolio', 'dividend', 'financial statement', 'balance sheet', 'income statement', 'cash flow statement', 'statement of retained earnings', 'financial ratio', 'valuation', 'bond', 'stock', 'mutual fund', 'exchange-traded fund', 'hedge fund', 'private equity', 'venture capital', 'mergers and acquisitions', 'initial public offering', 'secondary market', 'primary market', 'securities', 'derivative', 'option', 'futures', 'forward contract', 'swaps', 'commodities', 'credit rating', 'credit score', 'credit report', 'credit bureau', 'credit history', 'credit limit', 'credit utilization', 'credit counseling', 'credit card', 'debit card', 'ATM', 'bankruptcy', 'foreclosure', 'debt consolidation', 'taxes', 'tax return', 'tax deduction', 'tax credit', 'tax bracket', 'taxable income']

banking_capital_markets_keywords = ['bank', 'credit union', 'savings and loan association', 'commercial bank', 'investment bank', 'retail bank', 'wholesale bank', 'online bank', 'mobile banking', 'checking account', 'savings account', 'money market account', 'certificate of deposit', 'loan', 'mortgage', 'home equity loan', 'line of credit', 'credit card', 'debit card', 'ATM', 'automated clearing house', 'wire transfer', 'ACH', 'SWIFT', 'international banking', 'foreign exchange', 'forex', 'currency exchange', 'central bank', 'Federal Reserve', 'interest rate', 'inflation', 'deflation', 'monetary policy', 'fiscal policy', 'quantitative easing', 'securities', 'stock', 'bond', 'mutual fund', 'exchange-traded fund', 'hedge fund', 'private equity', 'venture capital', 'investment management', 'portfolio management', 'wealth management', 'financial planning']

healthcare_life_sciences_keywords = ['medical device', 'pharmaceutical', 'biotechnology', 'clinical trial', 'FDA', 'healthcare provider', 'healthcare plan', 'healthcare insurance', 'patient', 'doctor', 'nurse', 'pharmacist', 'hospital', 'clinic', 'healthcare system', 'healthcare policy', 'public health', 'healthcare IT', 'electronic health record', 'telemedicine', 'personalized medicine', 'genomics', 'proteomics', 'clinical research', 'drug development', 'drug discovery', 'medicine', 'health']

law_keywords = ['law', 'legal', 'attorney', 'lawyer', 'litigation', 'arbitration', 'dispute resolution', 'contract law', 'intellectual property', 'corporate law', 'labor law', 'tax law', 'real estate law', 'environmental law', 'criminal law', 'family law', 'immigration law', 'bankruptcy law']

sports_keywords = ['sports', 'football', 'basketball', 'baseball', 'hockey', 'soccer', 'golf', 'tennis', 'olympics', 'athletics', 'coaching', 'sports management', 'sports medicine', 'sports psychology', 'sports broadcasting', 'sports journalism', 'esports', 'fitness']

media_keywords = ['media', 'entertainment', 'film', 'television', 'radio', 'music', 'news', 'journalism', 'publishing', 'public relations', 'advertising', 'marketing', 'social media', 'digital media', 'animation', 'graphic design', 'web design', 'video production']

manufacturing_keywords = ['manufacturing', 'production', 'assembly', 'logistics', 'supply chain', 'quality control', 'lean manufacturing', 'six sigma', 'industrial engineering', 'process improvement', 'machinery', 'automation', 'aerospace', 'automotive', 'chemicals', 'construction materials', 'consumer goods', 'electronics', 'semiconductors']

automotive_keywords = ['automotive', 'cars', 'trucks', 'SUVs', 'electric vehicles', 'hybrid vehicles', 'autonomous vehicles', 'car manufacturing', 'automotive design', 'car dealerships', 'auto parts', 'vehicle maintenance', 'car rental', 'fleet management', 'telematics']

telecom_keywords = ['telecom', 'telecommunications', 'wireless', 'networks', 'internet', 'broadband', 'fiber optics', '5G', 'telecom infrastructure', 'telecom equipment', 'VoIP', 'satellite communications', 'mobile devices', 'smartphones', 'telecom services', 'telecom regulation', 'telecom policy']


information_technology_keywords = [
    "Artificial intelligence", "Machine learning", "Data Science", "Big Data", "Cloud Computing",
    "Cybersecurity", "Information security", "Network security", "Blockchain", "Cryptocurrency",
    "Internet of things", "IoT", "Web development", "Mobile development", "Frontend development",
    "Backend development", "Software engineering", "Software development", "Programming",
    "Database", "Data analytics", "Business intelligence", "DevOps", "Agile", "Scrum",
    "Product management", "Project management", "IT consulting", "IT service management", 
    "ERP", "CRM", "SaaS", "PaaS", "IaaS", "Virtualization", "Artificial reality", "AR", "Virtual reality",
    "VR", "Gaming", "E-commerce", "Digital marketing", "SEO", "SEM", "Content marketing",
    "Social media marketing", "User experience", "UX design", "UI design", "Cloud-native",
    "Microservices", "Serverless", "Containerization"
]

industries = {
    'Insurance': insurance_keywords,
    'Finance': finance_keywords,
    'Banking': banking_capital_markets_keywords,
    'Healthcare': healthcare_life_sciences_keywords,
    'Legal': law_keywords,
    'Sports': sports_keywords,
    'Media': media_keywords,
    'Manufacturing': manufacturing_keywords,
    'Automotive': automotive_keywords,
    'Telecom': telecom_keywords,
    'IT': information_technology_keywords
}

 
