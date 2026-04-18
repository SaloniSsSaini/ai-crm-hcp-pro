import { useEffect, useState } from "react";
import { api } from "../services/api";
import { BarChart, Bar, XAxis, YAxis } from "recharts";

export default function Dashboard() {
  const [data, setData] = useState([]);

  useEffect(() => {
    api.get("/analytics").then((res) => {
      setData([
        { name: "Total", value: res.data.total },
        { name: "Positive", value: res.data.positive }
      ]);
    });
  }, []);

  return (
    <div>
      <h2>📊 Analytics</h2>

      <BarChart width={300} height={200} data={data}>
        <XAxis dataKey="name" />
        <YAxis />
        <Bar dataKey="value" />
      </BarChart>
    </div>
  );
}