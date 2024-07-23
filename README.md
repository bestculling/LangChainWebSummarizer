## Text Summarization API with LangChain and FastAPI

This repository provides a simple FastAPI application that uses LangChain to summarize web pages. It leverages the power of Google Gemini Pro and offers language selection for Thai and English summaries. This project also demonstrates the use of LangChain's "stuff" chains for efficient text processing.

### Features

- **Web Page Summarization:**  Provides concise summaries of web page content.
- **Multilingual Support:**  Offers summaries in both Thai and English.
- **FastAPI Framework:**  Uses FastAPI for a modern and performant API experience.
- **Stuff Chains:** Utilizes LangChain's "stuff" chains for streamlined text processing.

### Stuff Chains Explained

In LangChain, "stuff" chains are used to insert all the documents retrieved by a loader into a single prompt. This is particularly useful when you want to summarize or analyze multiple documents together. 

In this project, the `stuff_chain` takes all the content from a web page, formats it using the `doc_prompt`, and then feeds it as a single input to the language model (Gemini Pro) along with the summarizing prompt. This allows the language model to consider the entire context of the web page when generating a summary.

![Stuff](https://js.langchain.com/v0.1/assets/images/stuff-818da4c66ee17911bc8861c089316579.jpg)
read more: https://js.langchain.com/v0.1/docs/modules/chains/document/stuff/

### Installation and Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/bestculling/LangChainWebSummarizer.git
   cd LangChainWebSummarizer
   ```

2. **Create a Virtual Environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Environment Variables:**
   - Create a `.env` file in the root directory.
   - Add your Google API key:
     ```
     GOOGLE_API_KEY=your_google_api_key
     ```

5. **Run the Application:**
   ```bash
   uvicorn main:app --reload 
   ```

### Usage

1. **Send a POST request to `/summarize` with the following JSON payload:**
   ```json
   {
     "url": "https://example.com/article-to-summarize",
     "language": "en" // "th" for Thai
   }
   ```
2. **The API will respond with the summary in JSON format:**
   ```json
   {
     "summary": "This is a concise summary of the web page content."
   }
   ```

### Example

```bash
curl -X POST -H "Content-Type: application/json" -d '{"url": "https://en.wikipedia.org/wiki/Artificial_intelligence", "language": "en"}' http://localhost:8000/summarize 
```

### Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have any improvements or bug fixes. 
