import React, { useState } from "react";
import axios from "axios";
import Header from "../components/Header";
import ChatMessage from "../components/ChatMessage";
import MessageInput from "../components/MessageInput";

const ChatInterface = () => {
  const [file, setFile] = useState(null);
  const [pdfData, setPdfData] = useState(null);
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [successMessage, setSuccessMessage] = useState("");

  const handleFileChange = (file) => {
    if (file) {
      setFile(file);
      setError(null);
    }
  };

  const handleUploadPdf = async () => {
    if (!file) {
      setError("Please select a PDF file.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      setLoading(true);
      setError(null);

      const response = await axios.post(
        "http://127.0.0.1:8000/api/v1/upload",
        formData,
        {
          headers: { "Content-Type": "multipart/form-data" },
        }
      );

      console.log("Upload response:", response.data); // Debugging log
      setPdfData(response.data);
      setMessages([
        ...messages,
        {
          id: Date.now(),
          type: "upload",
          content: `Uploaded PDF: ${response.data.filename}`,
        },
      ]);
      setError(null);
      setSuccessMessage("PDF uploaded successfully!"); // Set the success message
    } catch (error) {
      console.error("PDF upload failed:", error);
      setError(
        error.response?.data?.message ||
          "Failed to upload PDF. Please try again."
      );
      setSuccessMessage("");
    } finally {
      setLoading(false);
    }
  };

  const handleAskQuestion = async (question) => {
    if (!question) {
      setError("Please enter a question.");
      return;
    }

    if (!pdfData) {
      setError("No PDF data available. Please upload a PDF first.");
      return;
    }

    try {
      setLoading(true);
      setError(null);
      const response = await axios.post(
        "http://127.0.0.1:8000/api/v1/question",
        {
          pdf_id: pdfData.id,
          question: question,
        }
      );

      console.log("Question response:", response.data); // Debugging log
      const answer = response.data.answer;
      setMessages((prevMessages) => [
        ...prevMessages,
        { id: Date.now(), type: "user", content: question },
        { id: Date.now() + 1, type: "response", content: answer },
      ]);
    } catch (error) {
      console.error("Error asking question:", error);
      setError(
        error.response?.data?.message ||
          "Failed to get an answer. Please try again."
      );
    } finally {
      setLoading(false);
    }
  };

  const handleSendMessage = (message) => {
    if (!message.trim()) return;

    setMessages((prevMessages) => [
      ...prevMessages,
      { id: Date.now(), type: "user", content: message.trim() },
    ]);
    handleAskQuestion(message.trim());
  };

  return (
    <div className="min-h-screen bg-white flex flex-col">
      <Header onFileChange={handleFileChange} onUploadPdf={handleUploadPdf} />
      <main className="flex-1 w-full max-w-3xl mx-auto px-4">
        {successMessage && (
          <div className="bg-green-100 border border-green-500 text-green-700 px-4 py-2 rounded-md my-4">
            {successMessage}
          </div>
        )}
        {error && (
          <div className="bg-red-100 border border-red-500 text-red-700 px-4 py-2 rounded-md my-4">
            {error}
          </div>
        )}
        <div className="py-8">
          {loading && (
            <div className="text-center text-gray-500">Loading...</div>
          )}
          {messages.map((msg) => (
            <ChatMessage key={msg.id} type={msg.type} content={msg.content} />
          ))}
        </div>
      </main>
      <MessageInput onSend={handleSendMessage} />
    </div>
  );
};

export default ChatInterface;
