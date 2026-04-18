import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import { api } from "../../services/api";

export const sendMessage = createAsyncThunk(
  "chat/sendMessage",
  async (message) => {
    const res = await api.post("/chat", { message });
    return res.data;
  }
);

const chatSlice = createSlice({
  name: "chat",
  initialState: { response: "" },
  reducers: {},
  extraReducers: (builder) => {
    builder.addCase(sendMessage.fulfilled, (state, action) => {
      state.response = JSON.stringify(action.payload, null, 2);
    });
  }
});

export default chatSlice.reducer;