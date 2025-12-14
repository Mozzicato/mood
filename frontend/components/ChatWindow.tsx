import React, { useState, useEffect, useRef } from 'react';
import MessageBubble from './MessageBubble';

interface ChatWindowProps {
  emotion: string;
}

interface Message {
  role: 'user' | 'assistant';
  content: string;
}

const ChatWindow: React.FC<ChatWindowProps> = ({ emotion }) => {
  const [messages, setMessages] = useState<Message[]>([
    { role: 'assistant', content: `I'm here with you. Can you tell me more about what's been making you feel ${emotion.toLowerCase()}?` }
  ]);
  const [inputText, setInputText] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [isListening, setIsListening] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const recognitionRef = useRef<any>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(scrollToBottom, [messages]);

  useEffect(() => {
    if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {
        const SpeechRecognition = (window as any).SpeechRecognition || (window as any).webkitSpeechRecognition;
        recognitionRef.current = new SpeechRecognition();
        recognitionRef.current.continuous = false;
        recognitionRef.current.interimResults = false;
        recognitionRef.current.lang = 'en-US';

        recognitionRef.current.onresult = (event: any) => {
            const transcript = event.results[0][0].transcript;
            setInputText(prev => prev + (prev ? ' ' : '') + transcript);
            setIsListening(false);
        };

        recognitionRef.current.onerror = (event: any) => {
            console.error('Speech recognition error', event.error);
            setIsListening(false);
        };

        recognitionRef.current.onend = () => {
            setIsListening(false);
        };
    }
  }, []);

  const toggleListening = () => {
    if (!recognitionRef.current) {
        alert("Browser does not support speech recognition.");
        return;
    }

    if (isListening) {
        recognitionRef.current.stop();
        setIsListening(false);
    } else {
        recognitionRef.current.start();
        setIsListening(true);
    }
  };

  const sendMessage = async () => {
    if (!inputText.trim()) return;

    const userMessage = inputText;
    setMessages(prev => [...prev, { role: 'user', content: userMessage }]);
    setInputText('');
    setIsLoading(true);

    try {
      // Normalize backend base URL to prevent double "/chat"
      const baseUrl = (process.env.NEXT_PUBLIC_API_URL || 'https://mood-app-production-bbbc.up.railway.app').replace(/\/?$/, '');
      const apiUrl = `${baseUrl}/chat`;

      const response = await fetch(apiUrl, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          emotion: emotion,
          message: userMessage,
          history: messages.map(m => ({ role: m.role, content: m.content }))
        }),
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      const data = await response.json();
      setMessages(prev => [...prev, { role: 'assistant', content: data.message }]);
    } catch (error) {
      console.error('Error sending message:', error);
      setMessages(prev => [...prev, { role: 'assistant', content: "I'm having trouble connecting right now. Please try again." }]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="flex flex-col h-[600px] bg-white rounded-lg shadow-xl overflow-hidden max-w-2xl w-full mx-auto">
      <div className="bg-gray-100 p-4 border-b border-gray-200">
        <h2 className="text-lg font-semibold text-gray-700">TheraMood - {emotion} Support</h2>
      </div>
      
      <div className="flex-1 overflow-y-auto p-4">
        {messages.map((msg, index) => (
          <MessageBubble key={index} message={msg.content} isUser={msg.role === 'user'} />
        ))}
        {isLoading && (
           <div className="flex justify-start mb-4">
             <div className="bg-gray-200 text-gray-800 p-4 rounded-lg rounded-bl-none">
               Thinking...
             </div>
           </div>
        )}
        <div ref={messagesEndRef} />
      </div>

      <div className="p-4 border-t border-gray-200 bg-gray-50">
        <div className="flex gap-2">
          <input
            type="text"
            value={inputText}
            onChange={(e) => setInputText(e.target.value)}
            onKeyPress={(e) => e.key === 'Enter' && sendMessage()}
            placeholder="Type your message..."
            className="flex-1 p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 text-black"
            disabled={isLoading}
          />
          <button
            onClick={toggleListening}
            disabled={isLoading}
            className={`px-4 py-2 rounded-lg transition-colors ${
                isListening 
                ? 'bg-red-500 hover:bg-red-600 text-white' 
                : 'bg-gray-200 hover:bg-gray-300 text-gray-700'
            }`}
            title="Voice Input"
          >
            {isListening ? '⏹️' : '🎤'}
          </button>
          <button
            onClick={sendMessage}
            disabled={isLoading}
            className="bg-blue-500 text-white px-6 py-2 rounded-lg hover:bg-blue-600 disabled:bg-blue-300 transition-colors"
          >
            Send
          </button>
        </div>
      </div>
    </div>
  );
};

export default ChatWindow;
