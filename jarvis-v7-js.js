export default function JarvisUI() {
  return (
    <div className="min-h-screen bg-black text-white flex flex-col items-center justify-center overflow-hidden relative">
      {/* Background Glow */}
      <div className="absolute inset-0 bg-[radial-gradient(circle_at_center,_rgba(0,170,255,0.18),_transparent_55%)]" />

      {/* Header */}
      <div className="absolute top-6 left-6 text-cyan-300 text-xl font-bold tracking-[0.3em] opacity-80">
        JARVIS
      </div>

      {/* Animated Orb */}
      <div className="relative flex items-center justify-center">
        <div className="absolute w-96 h-96 rounded-full bg-cyan-400/10 blur-3xl animate-pulse" />

        <div className="absolute w-72 h-72 rounded-full border border-cyan-400/20 animate-spin" style={{ animationDuration: '18s' }} />

        <div className="absolute w-80 h-80 rounded-full border border-cyan-300/10 animate-spin" style={{ animationDirection: 'reverse', animationDuration: '24s' }} />

        <button
          className="relative w-44 h-44 rounded-full bg-cyan-400 shadow-[0_0_80px_rgba(34,211,238,0.8)] flex items-center justify-center text-black text-3xl font-bold hover:scale-105 transition-transform duration-300"
          onClick={() => alert('Connect this to your Python backend later using Flask/FastAPI + WebSockets ⚡')}
        >
          ◉
        </button>
      </div>

      {/* Status */}
      <div className="mt-12 text-center space-y-3">
        <h1 className="text-4xl font-bold tracking-wide text-cyan-200">
          Systems Online
        </h1>

        <p className="text-zinc-400 max-w-xl text-lg">
          Browser-based AI assistant interface with voice activation,
          animated orb visuals, text command support, and future Ollama integration.
        </p>
      </div>

      {/* Input Area */}
      <div className="mt-12 w-full max-w-2xl px-6">
        <div className="bg-zinc-900/80 border border-cyan-400/20 rounded-3xl p-4 backdrop-blur-xl shadow-2xl">
          <div className="flex items-center gap-3">
            <input
              placeholder="Type a command for Jarvis..."
              className="flex-1 bg-transparent outline-none text-lg text-white placeholder:text-zinc-500"
            />

            <button className="bg-cyan-400 text-black px-5 py-3 rounded-2xl font-semibold hover:bg-cyan-300 transition">
              Send
            </button>
          </div>
        </div>
      </div>

      {/* Bottom Feature Cards */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mt-16 w-full max-w-6xl px-8">
        <div className="bg-zinc-900/60 border border-cyan-400/10 rounded-3xl p-6 backdrop-blur-xl">
          <h2 className="text-cyan-300 text-xl font-semibold mb-2">
            Voice Commands
          </h2>
          <p className="text-zinc-400 leading-relaxed">
            Trigger actions with wake words, speech recognition, and natural commands.
          </p>
        </div>

        <div className="bg-zinc-900/60 border border-cyan-400/10 rounded-3xl p-6 backdrop-blur-xl">
          <h2 className="text-cyan-300 text-xl font-semibold mb-2">
            Session Modes
          </h2>
          <p className="text-zinc-400 leading-relaxed">
            Save and restore coding, study, chill, or productivity setups instantly.
          </p>
        </div>

        <div className="bg-zinc-900/60 border border-cyan-400/10 rounded-3xl p-6 backdrop-blur-xl">
          <h2 className="text-cyan-300 text-xl font-semibold mb-2">
            Local AI Brain
          </h2>
          <p className="text-zinc-400 leading-relaxed">
            Connect Ollama later for fully local AI reasoning without cloud APIs.
          </p>
        </div>
      </div>

      {/* Footer */}
      <div className="absolute bottom-4 text-zinc-600 text-sm tracking-wide">
        Browser JARVIS Interface • React + Tailwind + Future Python Backend
      </div>
    </div>
  )
}
