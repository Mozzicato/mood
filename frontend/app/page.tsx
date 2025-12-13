'use client';

import React, { useState } from 'react';
import EmotionCard from '@/components/EmotionCard';
import ChatWindow from '@/components/ChatWindow';

const emotions = [
  { name: 'Happy', color: 'bg-yellow-400', icon: '😊' },
  { name: 'Sad', color: 'bg-blue-500', icon: '😢' },
  { name: 'Angry', color: 'bg-red-500', icon: '😡' },
  { name: 'Overwhelmed', color: 'bg-purple-500', icon: '😰' },
  { name: 'Depressed', color: 'bg-gray-500', icon: '😞' },
  { name: 'Describe', color: 'bg-teal-500', icon: '✍️' },
];

export default function Home() {
  const [selectedEmotion, setSelectedEmotion] = useState<string | null>(null);

  const handleEmotionSelect = (emotion: string) => {
    setSelectedEmotion(emotion);
  };

  if (selectedEmotion) {
    return (
      <div className="min-h-screen bg-gray-50 p-8">
        <button 
            onClick={() => setSelectedEmotion(null)}
            className="mb-4 px-4 py-2 bg-gray-200 rounded hover:bg-gray-300 text-gray-800"
        >
            ← Back
        </button>
        <div className="mt-4">
            <ChatWindow emotion={selectedEmotion} />
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50 flex flex-col items-center justify-center p-8">
      <h1 className="text-4xl font-bold mb-2 text-gray-800">TheraMood AI</h1>
      <p className="text-xl text-gray-600 mb-12">How are you feeling today?</p>
      
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6 max-w-4xl w-full">
        {emotions.map((emotion) => (
          <EmotionCard
            key={emotion.name}
            emotion={emotion.name}
            color={emotion.color}
            icon={emotion.icon}
            onClick={handleEmotionSelect}
          />
        ))}
      </div>
    </div>
  );
}
