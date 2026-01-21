<section class="reveal">
  <h2>Live Microphone Noise Measurement</h2>
  <p><strong>Live Noise:</strong> <span id="live-noise" class="pulse">Inactive</span></p>
  <button onclick="startMic()">Start Measurement</button>
</section>

<script>
async function startMic() {
  try {
    // Request microphone access
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    const audioContext = new (window.AudioContext || window.webkitAudioContext)();
    const source = audioContext.createMediaStreamSource(stream);
    const analyser = audioContext.createAnalyser();
    analyser.fftSize = 2048;
    source.connect(analyser);

    const dataArray = new Uint8Array(analyser.fftSize);

    function measure() {
      // Get audio data
      analyser.getByteTimeDomainData(dataArray);

      // Calculate RMS (Root Mean Square) to estimate volume
      let sum = 0;
      for (let i = 0; i < dataArray.length; i++) {
        const sample = (dataArray[i] - 128) / 128; // normalize to [-1,1]
        sum += sample * sample;
      }
      const rms = Math.sqrt(sum / dataArray.length);
      const db = Math.round(20 * Math.log10(rms + 0.00001)); // add small value to avoid log(0)

      // Display dB on page
      document.getElementById("live-noise").innerText = `${db} dB (approx)`;

      requestAnimationFrame(measure);
    }

    measure();
  } catch (err) {
    document.getElementById("live-noise").innerText = "Microphone access denied";
    console.error(err);
  }
}
</script>
