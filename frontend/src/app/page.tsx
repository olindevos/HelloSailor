'use client';

import { useState } from 'react';

type Status = 'idle' | 'loading' | 'ok' | 'error';
type Metric = 'walked' | 'distance';

export default function Home() {
  const [status, setStatus] = useState<Status>('idle');
  const [message, setMessage] = useState<string>('');
  const [activeMetric, setActiveMetric] = useState<Metric | null>(null);

  async function fetchMetric(metric: Metric) {
    try {
      setStatus('loading');
      setActiveMetric(metric);
      const url = `${process.env.NEXT_PUBLIC_API_URL}/v1/stats/${metric}`;
      const res = await fetch(url);
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const data = await res.json();
      setMessage(JSON.stringify(data));
      setStatus('ok');
    } catch (err) {
      setMessage(String(err));
      setStatus('error');
    }
  }

  return (
    <main className="min-h-screen flex items-center justify-center">
      <div className="max-w-xl w-full rounded-xl border p-6 space-y-4">
        <h1 className="text-2xl font-semibold">Frontend ↔ Backend check</h1>

        <p className="text-sm text-gray-500">
          Backend URL: <code>{process.env.NEXT_PUBLIC_API_URL}</code>
        </p>

        <div className="flex gap-3">
          <button
            onClick={() => fetchMetric('walked')}
            className={`px-4 py-2 rounded-xl border ${activeMetric === 'walked' ? 'bg-gray-100' : ''}`}
          >
            Fetch walked
          </button>
          <button
            onClick={() => fetchMetric('distance')}
            className={`px-4 py-2 rounded-xl border ${activeMetric === 'distance' ? 'bg-gray-100' : ''}`}
          >
            Fetch distance
          </button>
        </div>

        {status === 'idle' && <p className="text-gray-500">Kies een metric hierboven.</p>}
        {status === 'loading' && <p>Bezig met ophalen…</p>}
        {status === 'ok' && (
          <p className="text-green-700">
            ✅ Succes ({activeMetric}): <code>{message}</code>
          </p>
        )}
        {status === 'error' && (
          <p className="text-red-700">
            ❌ Fout: <code>{message}</code>
          </p>
        )}
      </div>
    </main>
  );
}
