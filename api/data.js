let latestData = {
  aqi: "--",
  noise: "--",
  ph: "--",
  time: "--"
};

export default function handler(req, res) {
  if (req.method === "POST") {
    const { aqi, noise, ph } = req.body;

    latestData = {
      aqi,
      noise,
      ph,
      time: new Date().toISOString()
    };

    return res.status(200).json({ status: "ok" });
  }

  if (req.method === "GET") {
    return res.status(200).json(latestData);
  }

  res.status(405).end();
}

