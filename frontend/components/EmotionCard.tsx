import React from 'react';

interface EmotionCardProps {
  emotion: string;
  color: string;
  icon: string;
  onClick: (emotion: string) => void;
}

const EmotionCard: React.FC<EmotionCardProps> = ({ emotion, color, icon, onClick }) => {
  return (
    <div
      onClick={() => onClick(emotion)}
      className={`cursor-pointer p-6 rounded-xl shadow-lg hover:shadow-xl transition-transform transform hover:scale-105 flex flex-col items-center justify-center gap-4 h-48 text-white ${color}`}
    >
      <div className="text-6xl">{icon}</div>
      <h2 className="text-2xl font-bold">{emotion}</h2>
    </div>
  );
};

export default EmotionCard;
