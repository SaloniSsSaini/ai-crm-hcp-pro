import ChatPanel from "./components/ChatPanel";
import InteractionForm from "./components/InteractionForm";
import Dashboard from "./components/Dashboard";
import VoiceRecorder from "./components/VoiceRecorder";

function App() {
  return (
    <div style={{ fontFamily: "Inter, sans-serif" }}>
      <h1>🚀 AI CRM (Pro)</h1>

      <ChatPanel />
      <VoiceRecorder />
      <InteractionForm />
      <Dashboard />
    </div>
  );
}

export default App;