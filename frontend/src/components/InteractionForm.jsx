import { useDispatch } from "react-redux";
import { saveInteraction } from "../features/interaction/interactionSlice";
import { useState } from "react";

export default function InteractionForm() {
  const dispatch = useDispatch();

  const [data, setData] = useState({
    hcp_name: "",
    summary: "",
    sentiment: "",
    follow_up: ""
  });

  return (
    <div style={{ padding: 20 }}>
      <h2>📋 Log Interaction</h2>

      <input
        placeholder="HCP Name"
        onChange={(e) =>
          setData({ ...data, hcp_name: e.target.value })
        }
      />

      <input
        placeholder="Summary"
        onChange={(e) =>
          setData({ ...data, summary: e.target.value })
        }
      />

      <button onClick={() => dispatch(saveInteraction(data))}>
        Save
      </button>
    </div>
  );
}