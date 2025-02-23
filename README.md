# Vendor Search System

A Streamlit-based application that allows users to search for vendors using semantic search powered by Qdrant vector database and OpenAI embeddings.

## Features

- Semantic search for vendors using natural language queries
- Vector similarity search using Qdrant
- Email integration with Brevo API
- Interactive UI built with Streamlit
- Real-time search results with relevance scores

## Setup

1. Clone the repository:
```bash
git clone <your-repo-url>
cd heineken2
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables in `.env`:
```
OPENAI_API_KEY=your_openai_api_key
QDRANT_URL=your_qdrant_url
QDRANT_API_KEY=your_qdrant_api_key
BREVO_API_KEY=your_brevo_api_key
```

4. Run the application:
```bash
streamlit run search_qdrant.py
```

## Usage

1. Enter a search query describing the type of vendor you're looking for
2. View matching vendors with their relevance scores
3. Send emails to vendors directly from the interface

## Tech Stack

- Python 3.8+
- Streamlit
- OpenAI Embeddings
- Qdrant Vector Database
- Brevo Email API
- python-dotenv

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
