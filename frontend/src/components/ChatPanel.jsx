import { useDispatch, useSelector } from "react-redux";
import { sendMessage } from "../features/chat/chatSlice";
import { useState } from "react";

export default function ChatPanel() {
  const dispatch = useDispatch();
  const response = useSelector((s) => s.chat.response);
  const [msg, setMsg] = useState("");

  return (
    <div style={{ padding: 20, border: "1px solid #ccc" }}>
      <h2>🤖 AI Assistant</h2>

      <input
        placeholder="Type message..."
        onChange={(e) => setMsg(e.target.value)}
      />

      <button onClick={() => dispatch(sendMessage(msg))}>
        Send
      </button>

      <pre>{response}</pre>
    </div>
  );
}