'use client';

import { useEffect, useState } from 'react';

type Status = 'loading' | 'ok' | 'error';

export default function Home() {
  const [status, setStatus] = useState<Status>('loading');
  const [message, setMessage] = useState<string>('');

  useEffect(() => {
    const url = `${process.env.NEXT_PUBLIC_API_URL}/v1/strava/ping`;
    fetch(url)
      .then(async (res) => {
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        const data = await res.json();
        setMessage(JSON.stringify(data));
        setStatus('ok');
      })
      .catch((err) => {
        setMessage(String(err));
        setStatus('error');
      });
  }, []);

  return (
    <main className="min-h-screen flex items-center justify-center">
      <div className="max-w-xl w-full rounded-xl border p-6">
        <p className="text-sm text-gray-500 mb-2">
          Backend URL: <code>{process.env.NEXT_PUBLIC_API_URL}</code>
        </p>
        {status === 'loading' && <p>Bezig met ophalen…</p>}
        {status === 'ok' && (
          <p className="text-green-700">
            ✅ Succes: <code>{message}</code>
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
