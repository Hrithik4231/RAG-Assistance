import { useState, useRef, useEffect } from "react";
import axios from "axios";

import "./App.css";

function App() {
  const [file, setFile] = useState(null);
  const [fileName, setFileName] = useState("No file chosen");
  const [messages, setMessages] = useState([]);
  const [query, setQuery] = useState("");
  const [loading, setLoading] = useState(false);
  const [uploadMessage, setUploadMessage] = useState("");
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  // Handle PDF Upload
  const handleUpload = async () => {
    if (!file) {
      alert("Please select a PDF file");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      setLoading(true);
      const res = await axios.post("http://localhost:8000/upload", formData);
      setUploadMessage(res.data.message);
      setFile(null);
      setFileName("No file chosen");
    } catch (error) {
      console.error(error);
      setUploadMessage("Upload failed");
    } finally {
      setLoading(false);
    }
  };

  // Handle Chat
  const handleAsk = async () => {
    if (!query.trim()) return;

    const userMessage = query;
    setQuery("");
    setMessages((prev) => [...prev, { type: "user", content: userMessage }]);

    try {
      setLoading(true);
      const res = await axios.get("http://localhost:8000/chat", {
        params: { query: userMessage },
      });

      setMessages((prev) => [
        ...prev,
        { type: "ai", content: res.data.answer },
      ]);
    } catch (error) {
      console.error(error);
      setMessages((prev) => [
        ...prev,
        { type: "ai", content: "Error getting response. Please try again." },
      ]);
    } finally {
      setLoading(false);
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleAsk();
    }
  };

  return (
    <div className="app-container">
      {/* Header */}
      <header className="header">
        <div className="header-content">
          <h1>RAG AI Assistant</h1>
        </div>
      </header>

      {/* Main Chat Area */}
      <main className="chat-container">
        {messages.length === 0 ? (
          <div className="empty-state">
            <h2>Welcome to RAG AI Assistant</h2>
            <p>Upload a PDF and start asking questions!</p>
          </div>
        ) : (
          <div className="messages-list">
            {messages.map((msg, idx) => (
              <div key={idx} className={`message ${msg.type}`}>
                <div className="message-content">
                  {msg.type === "user" ? (
                    <div className="user-icon">👤</div>
                  ) : (
                    <div className="ai-icon">🤖</div>
                  )}
                  <p>{msg.content}</p>
                </div>
              </div>
            ))}
            {loading && (
              <div className="message ai">
                <div className="message-content">
                  <div className="ai-icon">🤖</div>
                  <div className="typing-indicator">
                    <span></span>
                    <span></span>
                    <span></span>
                  </div>
                </div>
              </div>
            )}
            <div ref={messagesEndRef} />
          </div>
        )}
      </main>

      {/* Input Area */}
      <footer className="input-footer">
        <div className="input-container">
          <div className="upload-area">
            <input
              type="file"
              id="file-input"
              accept=".pdf"
              onChange={(e) => {
                setFile(e.target.files[0]);
                setFileName(e.target.files[0]?.name || "No file chosen");
              }}
            />
            <button
              className="plus-btn"
              onClick={() => document.getElementById("file-input").click()}
              title="Upload PDF"
              disabled={loading}
            >
              +
            </button>
            {uploadMessage && (
              <span className="upload-message-inline">{uploadMessage}</span>
            )}
          </div>
          <textarea
            className="message-input"
            placeholder="Ask a question about your PDF... (Shift+Enter for new line)"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            onKeyPress={handleKeyPress}
            disabled={loading}
            rows="1"
          />
          <button
            className="send-btn"
            onClick={handleAsk}
            disabled={loading || !query.trim()}
          >
            ➤
          </button>
        </div>
      </footer>
    </div>
  );
}

export default App;