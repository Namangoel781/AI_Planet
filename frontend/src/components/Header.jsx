import React, { useState } from "react";
import Logo from "../assets/Logo.png";

const Header = ({ onFileChange, onUploadPdf }) => {
  const [fileName, setFileName] = useState("");

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      setFileName(file.name);
      onFileChange(file);
      onUploadPdf();
    }
  };

  return (
    <header className="border-b shadow-lg bg-gray-100">
      <div className="max-w-7xl mx-auto px-4 py-3 flex justify-between items-center">
        <div className="flex items-center gap-2">
          <div className="w-20 h-12 sm:w-20 sm:h-10 md:w-24 md:h-12 lg:w-32 lg:h-12 rounded-full flex items-center justify-center">
            <img
              src={Logo}
              alt="Planet Logo"
              className="w-full h-full object-contain"
            />
          </div>
        </div>
        <div className="flex items-center gap-4">
          {fileName && (
            <div className="flex items-center gap-2 text-sm text-green-600 mr-2">
              {/* SVG icon */}
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="20"
                height="20"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                strokeWidth="1"
                strokeLinecap="round"
                strokeLinejoin="round"
                className="lucide lucide-files"
              >
                <path d="M20 7h-3a2 2 0 0 1-2-2V2" />
                <path d="M9 18a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h7l4 4v10a2 2 0 0 1-2 2Z" />
                <path d="M3 7.6v12.8A1.6 1.6 0 0 0 4.6 22h9.8" />
              </svg>
              {/* File name */}
              <span>{fileName}</span>
            </div>
          )}
          <label
            htmlFor="upload-pdf"
            className="flex items-center gap-2 px-3 py-1.5 text-sm border rounded-lg border-black hover:bg-gray-50 cursor-pointer font-semibold"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="20"
              height="20"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              strokeWidth="1.25"
              strokeLinecap="round"
              strokeLinejoin="round"
              className="lucide lucide-circle-plus"
            >
              <circle cx="12" cy="12" r="10" />
              <path d="M8 12h8" />
              <path d="M12 8v8" />
            </svg>
            Upload PDF
          </label>
          <input
            type="file"
            id="upload-pdf"
            style={{ display: "none" }}
            onChange={handleFileChange}
          />
        </div>
      </div>
    </header>
  );
};

export default Header;
