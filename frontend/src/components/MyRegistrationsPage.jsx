import React, { useState } from 'react';
import { ChevronLeft, MapPin, Clock, Users, Bookmark, Bell, HelpCircle } from 'lucide-react';

export default function MyRegistrationsPage({ onNavigate, user }) {
  const [activeTab, setActiveTab] = useState('going');

  return (
    <div className="min-h-screen bg-slate-900">
      {/* Header */}
      <header className="bg-gray-800 border-b border-gray-700">
        <div className="max-w-7xl mx-auto px-6 py-4 flex items-center justify-between">
          <div className="flex items-center gap-8">
            <div className="text-2xl font-bold text-primary-500">InfiniteBZ</div>
            <div className="hidden md:flex items-center gap-3 bg-gray-100 rounded-full px-4 py-2 flex-1">
              <input
                type="text"
                placeholder="Search events..."
                className="bg-transparent outline-none flex-1"
              />
            </div>
            <div className="flex items-center gap-2 bg-gray-100 rounded-full px-4 py-2">
              <MapPin size={18} className="text-gray-600" />
              <span>Chennai, IN</span>
              <span className="text-gray-400">×</span>
            </div>
            <button className="bg-gray-800 text-white rounded-full p-2">
              🔍
            </button>
          </div>
          <div className="flex items-center gap-4">
            <span className="text-sm font-semibold">30% off</span>
            <button className="flex items-center gap-2 bg-primary-500 hover:bg-primary-600 text-slate-900 px-4 py-2 rounded-lg font-bold transition-all shadow-lg shadow-primary-500/20">
              Try Pro
            </button>
            <button className="flex items-center gap-2 bg-primary-500 hover:bg-primary-600 text-slate-900 px-4 py-2 rounded-lg font-bold transition-all shadow-lg shadow-primary-500/20">
              Free
            </button>

            <div className="w-10 h-10 rounded-full overflow-hidden flex items-center justify-center">
              {user?.profile_image ? (
                <img
                  src={user.profile_image}
                  alt="Profile"
                  className="w-full h-full object-cover"
                />
              ) : (
                <div className="w-full h-full bg-primary-500 flex items-center justify-center text-slate-900 font-bold">
                  {user?.full_name?.[0] || 'U'}
                </div>
              )}
            </div>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-6 py-8">
        {/* Back Link */}
        <button
          onClick={onNavigate}
          className="flex items-center gap-2 text-slate-300 mb-8 hover:text-white"
        >
          <ChevronLeft size={20} />
          Back to home page
        </button>

        {/* Title and Actions */}
        <div className="flex justify-between items-start mb-8">
          <h1 className="text-5xl font-bold text-white">Your events</h1>
          <button className="flex items-center gap-2 bg-primary-500 hover:bg-primary-600 text-slate-900 px-4 py-2 rounded-lg font-bold transition-all shadow-lg shadow-primary-500/20">
            📅 Add to calendar
          </button>
        </div>

        {/* Tabs */}
        <div className="flex gap-4 mb-8">
          <button
            onClick={() => setActiveTab('going')}
            className={`flex items-center gap-2 px-6 py-3 rounded-full font-semibold transition ${
              activeTab === 'going'
                ? 'bg-primary-500 text-slate-900'
                : 'bg-white text-gray-800 border border-gray-300 hover:bg-gray-50'
            }`}
          >
            ✓ Going
          </button>
          <button
            onClick={() => setActiveTab('saved')}
            className={`flex items-center gap-2 px-6 py-3 rounded-full font-semibold transition ${
              activeTab === 'saved'
                ? 'bg-primary-500 text-slate-900'
                : 'bg-white text-gray-800 border border-gray-300 hover:bg-gray-50'
            }`}
          >
            📌 Saved
          </button>
          <button
            onClick={() => setActiveTab('past')}
            className={`flex items-center gap-2 px-6 py-3 rounded-full font-semibold transition ${
              activeTab === 'past'
                ? 'bg-primary-500 text-slate-900'
                : 'bg-white text-gray-800 border border-gray-300 hover:bg-gray-50'
            }`}
          >
            ↩ Past
          </button>
        </div>

        {/* Filter */}
        <div className="mb-6">
          <button className="flex items-center gap-2 text-slate-300 hover:text-white">
            📅 From today <span className="ml-2">∨</span>
          </button>
        </div>

        {/* Events */}
        <div>
          <div className="text-sm text-slate-400 mb-6 font-semibold">MON, JAN 12</div>

          {/* Event Card */}
          <div className="bg-white rounded-3xl overflow-hidden shadow-sm hover:shadow-md transition max-w-md">
            <div className="relative h-48 bg-gradient-to-r from-orange-400 to-orange-600 flex items-center justify-center">
              <div className="absolute top-4 left-4 bg-green-100 text-green-700 px-3 py-1 rounded-full text-sm font-semibold flex items-center gap-1">
                ● Going
              </div>
              <button className="absolute top-4 right-4 bg-white rounded-lg p-2 hover:bg-gray-100">
                📌
              </button>
              <div className="text-center">
                <div className="flex justify-center gap-3 mb-4">
                  <div className="w-10 h-10 rounded-full bg-yellow-600 flex items-center justify-center text-2xl">👨</div>
                  <div className="w-10 h-10 rounded-full bg-orange-600 flex items-center justify-center text-2xl">👨</div>
                  <div className="w-10 h-10 rounded-full bg-gray-800 flex items-center justify-center text-2xl">🐺</div>
                  <div className="w-10 h-10 rounded-full bg-yellow-700 flex items-center justify-center text-2xl">👨</div>
                  <div className="w-10 h-10 rounded-full bg-red-600 flex items-center justify-center text-2xl">👩</div>
                </div>
                <p className="text-white text-lg font-bold">More Than<br />Family</p>
              </div>
            </div>

            <div className="p-6">
              <h3 className="text-xl font-bold text-gray-900 mb-3">
                Find Partners, Recruit, or Collaborate – New on Ronda Jobs India!
              </h3>

              <div className="space-y-2 text-sm text-gray-700 mb-4">
                <div className="flex items-center gap-2">
                  <span>Mon, Jan 12 · 9:00 AM IST</span>
                  <span className="text-red-500">●</span>
                  <span className="text-gray-600">Online</span>
                </div>
                <div>
                  by <span className="font-semibold">Ronda Night</span> - <span className="text-gray-600">Exciting Dating event · 3.1</span>
                  <span className="text-red-500 ml-1">⭐</span>
                </div>
              </div>

              <div className="flex items-center gap-2 text-gray-700 font-semibold">
                <Users size={18} />
                <span>9 attendees</span>
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}