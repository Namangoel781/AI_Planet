import React from "react";
import img from "../assets/ai_planet.png";

const ChatMessage = ({ type, content }) => (
  <div className="flex gap-4 mb-6">
    <div
      className={`w-10 h-10 rounded-full flex items-center justify-center flex-shrink-0 ${
        type === "user"
          ? "bg-purple-100 text-purple-600"
          : "bg-green-100 text-green-600"
      }`}
    >
      {type === "user" ? (
        <span className="text-lg font-semibold">U</span>
      ) : (
        <img
          src={img}
          alt="AI Planet"
          className="w-8 h-8 object-cover rounded-full"
        />
      )}
    </div>

    <div className="flex-1">
      <p
        className={`text-base ${
          type === "user" ? "text-gray-700" : "text-gray-700"
        } font-medium text-base leading-relaxed`}
      >
        {content}
      </p>
    </div>
  </div>
);

export default ChatMessage;
