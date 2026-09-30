# AI-Powered-Legal-Document-Generator | LegalEase

LegalEase leverages state-of-the-art Generative AI to simplify the creation of legal documents by providing customizable, accurate, and editable templates for a wide range of use cases.

Users can generate employment contracts, lease agreements, NDAs, and more — all tailored to their specific inputs like involved parties, effective dates, and key terms.

Built with FastAPI and integrated with a powerful AI core, LegalEase ensures users receive professional-grade legal documents that maintain formatting standards, include custom branding (such as logos and fonts), and support features like editable previews and automatic term tables.

With secure handling of sensitive user data and seamless document export options (PDF, DOCX, TXT), the platform bridges the gap between accessibility and legal professionalism.

LegalEase empowers entrepreneurs, professionals, and individuals to generate reliable legal content confidently — without needing a legal background.

## Contents
- About The Project
- Key Features
- Tech Stack
- Installation
- Usage Scenarios
- Project Structure
- Disclaimer
- License

## Key Features
- AI-Powered Document Generation
- Customizable Templates
- Custom Branding (Logo, Fonts)
- Editable Live Preview
- Automatic Term Tables
- Export as PDF, DOCX, TXT
- Secure Data Handling

## Tech Stack
- Backend: FastAPI (Python)
- AI Core: Generative AI (LLM)
- Document Export: ReportLab, python-docx

## Installation
1. Clone the repository
   git clone https://github.com/your-username/AI-Powered-Legal-Document-generator.git
2. Create virtual environment
   python -m venv venv
3. Activate it
   venv\Scripts\activate
4. Install dependencies
   pip install -r requirements.txt
5. Run the app
   uvicorn main:app --reload

Open in browser: http://127.0.0.1:8000

## Usage Scenarios

**Scenario 1 - Startup Founder:** Selects "Employment Contract", enters new hire details. Gets agreement with roles, salary, confidentiality clauses. Adds company logo and downloads as branded PDF.

**Scenario 2 - Freelancer:** Needs an NDA for a client. Enters parties, scope, and effective date to get instant legally structured NDA.

**Scenario 3 - Landlord:** Enters property address and tenant details to generate a formatted residential lease agreement, downloadable as DOCX.

## Disclaimer
This tool provides drafts for informational purposes only and does not constitute legal advice. Consult a qualified attorney for review.

## License
MIT License
