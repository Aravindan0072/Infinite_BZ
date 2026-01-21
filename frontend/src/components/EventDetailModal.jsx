import { useState, useEffect } from 'react';
import {
    Calendar, MapPin, Clock, User, Mail, Ticket, Globe, X, Share2, Heart,
    CheckCircle2, ArrowRight, Linkedin, Twitter, Shield, Star, LayoutGrid
} from 'lucide-react';

export default function EventDetailModal({ event, isOpen, onClose, onRegister, isRegistered }) {
    if (!isOpen || !event) return null;

    const [activeTab, setActiveTab] = useState('about');
    const [isFollowing, setIsFollowing] = useState(false);
    const [isLoadingFollow, setIsLoadingFollow] = useState(false);
    const [isLoadingCheckFollow, setIsLoadingCheckFollow] = useState(false);
    const isInternal = event.raw_data?.source === 'InfiniteBZ';
    const isOnline = event.online_event || event.mode === 'online';

    // Check if user is already following this organizer when event changes
    useEffect(() => {
        if (event?.organizer_email) {
            checkFollowStatus();
        }
    }, [event?.organizer_email]);

    const checkFollowStatus = async () => {
        if (!event?.organizer_email) return;

        setIsLoadingCheckFollow(true);
        try {
            const token = localStorage.getItem('token');
            const response = await fetch(`http://localhost:8000/api/v1/user/following`, {
                method: 'GET',
                headers: {
                    'Authorization': `Bearer ${token}`,
                }
            });

            if (response.ok) {
                const data = await response.json();
                const isFollowingOrganizer = data.following.some(user => user.email === event.organizer_email);
                setIsFollowing(isFollowingOrganizer);
            }
        } catch (error) {
            console.error('Error checking follow status:', error);
        } finally {
            setIsLoadingCheckFollow(false);
        }
    };

    // Mock Data for Enhanced UI
    const speakers = [
        { name: "Arjun Varun", role: "CEO, Z-Corp", image: "https://i.pravatar.cc/150?u=arjun" },
        { name: "Meera Reddy", role: "Founder, ScaleUp", image: "https://i.pravatar.cc/150?u=meera" },
        { name: "David Chen", role: "CTO, TechFlow", image: "https://i.pravatar.cc/150?u=david" }
    ];

    const agenda = [
        { time: "10:00 AM", title: "Registration & Networking", desc: "Pick up your badge and meet fellow attendees." },
        { time: "11:00 AM", title: "Keynote: Future of Tech", desc: "Deep dive into 2024 trends with industry leaders." },
        { time: "01:00 PM", title: "Lunch Break", desc: "Gourmet lunch provided at the venue." },
        { time: "02:30 PM", title: "Workshops", desc: "Hands-on sessions on AI, Marketing, and Sales." }
    ];

    const handleFollow = async () => {
        console.log('=== FOLLOW BUTTON CLICKED ===');
        console.log('Event object:', event);
        console.log('Organizer email:', event?.organizer_email);
        console.log('Organizer name:', event?.organizer_name);
        console.log('Current following status:', isFollowing);

        // Use organizer_email if available, otherwise try to find user by name
        let targetIdentifier = event?.organizer_email;

        if (!targetIdentifier) {
            // Fallback: try to use organizer name to find the user
            console.log('No organizer email, trying to find user by name');
            targetIdentifier = event?.organizer_name;
        }

        if (!targetIdentifier) {
            console.error('❌ ERROR: No organizer email or name available');
            alert('Cannot identify the event organizer. Please try a different event.');
            return;
        }

        // If already following, don't do anything (one-way follow)
        if (isFollowing) {
            console.log('ℹ️ Already following this organizer, no action needed');
            return;
        }

        setIsLoadingFollow(true);
        console.log('⏳ Starting follow request...');

        try {
            const token = localStorage.getItem('token');
            console.log('Token exists:', !!token);

            if (!token) {
                console.error('❌ ERROR: No authentication token found');
                alert('You must be logged in to follow organizers.');
                return;
            }

            const url = `http://localhost:8000/api/v1/user/follow/${encodeURIComponent(targetIdentifier)}`;
            console.log('🌐 Making POST request to:', url);

            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    'Authorization': `Bearer ${token}`,
                    'Content-Type': 'application/json',
                }
            });

            console.log('📡 Response status:', response.status);
            console.log('📡 Response headers:', Object.fromEntries(response.headers.entries()));

            if (response.ok) {
                console.log('✅ Successfully followed organizer!');
                setIsFollowing(true);

                // Show success message
                alert('Successfully followed the organizer!');
            } else {
                const errorText = await response.text();
                console.error('❌ Failed to follow user:', response.status, errorText);

                // Show error to user
                alert(`Failed to follow organizer. Error: ${response.status} - ${errorText}`);
            }
        } catch (error) {
            console.error('❌ Network error following user:', error);
            alert('Network error occurred. Please check your connection and try again.');
        } finally {
            setIsLoadingFollow(false);
            console.log('🏁 Follow request completed');
        }
    };

    return (
        <div className="fixed inset-0 z-50 bg-slate-900 animate-in fade-in duration-200 overflow-hidden">
            {/* Full Screen Container */}
            <div className="w-full h-full flex flex-col relative">

                {/* Close Button - Floated fixed top right */}
                <button
                    onClick={onClose}
                    className="absolute top-6 right-6 z-50 p-2.5 bg-black/40 hover:bg-black/60 text-white rounded-full backdrop-blur-md transition-all border border-white/10 group"
                >
                    <X size={24} className="group-hover:rotate-90 transition-transform" />
                </button>

                <div className="flex-1 flex overflow-hidden">
                    {/* LEFT SIDE - VISUALS & KEY INFO (45% Width) */}
                    <div className="hidden lg:flex w-[45%] h-full relative flex-col">
                        {/* Background Image with Overlay */}
                        <div className="absolute inset-0">
                            {event.image_url ? (
                                <img src={event.image_url} alt={event.title} className="w-full h-full object-cover" />
                            ) : (
                                <div className="w-full h-full bg-gradient-to-br from-slate-900 to-slate-800" />
                            )}
                            <div className="absolute inset-0 bg-gradient-to-t from-slate-900 via-slate-900/60 to-transparent" />
                            <div className="absolute inset-0 bg-gradient-to-r from-slate-900/80 to-transparent" />
                        </div>

                        {/* Content Overlay */}
                        <div className="relative z-10 p-12 mt-auto">
                            <div className="flex items-center gap-3 mb-6">
                                <span className={`px-4 py-1.5 rounded-full text-xs font-bold uppercase tracking-wide border backdrop-blur-md ${event.is_free
                                    ? 'bg-green-500/20 text-green-400 border-green-500/30'
                                    : 'bg-orange-500/20 text-orange-400 border-orange-500/30'
                                    }`}>
                                    {event.is_free ? 'Free Entry' : 'Paid Ticket'}
                                </span>
                                <span className="px-4 py-1.5 rounded-full bg-white/10 text-white text-xs font-bold uppercase tracking-wide border border-white/10 backdrop-blur-md">
                                    {isOnline ? 'Online Event' : 'In Person'}
                                </span>
                            </div>
                            <h1 className="text-5xl font-extrabold text-white mb-4 leading-tight">
                                {event.title}
                            </h1>
                            <p className="text-xl text-slate-300 font-medium flex items-center gap-2">
                                Hosted by <span className="text-white">{event.organizer_name}</span>
                            </p>
                        </div>
                    </div>

                    {/* RIGHT SIDE - SCROLLABLE DETAILS & REGISTRATION (55% Width) */}
                    <div className="flex-1 h-full overflow-y-auto bg-slate-900 custom-scrollbar relative">
                        <div className="p-8 md:p-12 max-w-3xl mx-auto space-y-12">

                            {/* Mobile Header (Visible only on small screens) */}
                            <div className="lg:hidden mb-8">
                                <img src={event.image_url} className="w-full h-64 object-cover rounded-2xl mb-6" />
                                <h1 className="text-3xl font-bold text-white mb-2">{event.title}</h1>
                            </div>

                            {/* KEY DETAILS GRID */}
                            <div className="grid grid-cols-1 md:grid-cols-2 gap-6 p-6 bg-slate-800/50 rounded-2xl border border-slate-700/50">
                                <div className="flex items-start gap-4">
                                    <div className="p-3 rounded-lg bg-slate-800 text-primary-500 border border-slate-700">
                                        <Calendar size={24} />
                                    </div>
                                    <div>
                                        <p className="text-sm text-slate-400 font-medium uppercase tracking-wide mb-1">Date & Time</p>
                                        <p className="text-white font-bold text-lg">
                                            {new Date(event.start_time).toLocaleDateString(undefined, { weekday: 'short', month: 'short', day: 'numeric' })}
                                        </p>
                                        <p className="text-slate-400">
                                            {new Date(event.start_time).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
                                        </p>
                                    </div>

                                    <button
                                        onClick={() => {
                                            if (!isRegistered) {
                                                onRegister(event);
                                                // onClose(); // Optional: keep open to show success state
                                            }
                                        }}
                                        disabled={isRegistered}
                                        className={`w-full py-4 rounded-xl font-bold text-lg flex items-center justify-center gap-2 transition-all duration-300 ${isRegistered
                                            ? 'bg-green-500/20 text-green-400 border border-green-500/50 cursor-default'
                                            : 'bg-gradient-to-r from-primary-600 to-indigo-600 hover:from-primary-500 hover:to-indigo-500 text-white shadow-lg shadow-primary-500/25 hover:shadow-primary-500/50 hover:-translate-y-0.5'
                                            }`}
                                    >
                                        {isRegistered ? (
                                            <> <CheckCircle2 className="animate-in zoom-in spin-in-180" /> Registered </>
                                        ) : (
                                            <> <Ticket className="animate-pulse" /> Auto-Register </>
                                        )}
                                    </button>

                                    {/* Follow Button - Moved here under Auto-Register */}
                                    <div className="mt-4 pt-4 border-t border-slate-700/50">
                                        <button
                                            onClick={handleFollow}
                                            disabled={isLoadingFollow}
                                            className={`w-full py-3 rounded-xl font-medium text-sm flex items-center justify-center gap-2 transition-all duration-300 ${isFollowing
                                                ? 'bg-green-500/20 text-green-400 border border-green-500/50 hover:bg-green-500/30'
                                                : 'bg-slate-700/50 text-white hover:bg-slate-600 border border-slate-600/50'
                                                }`}
                                        >
                                            {isLoadingFollow ? 'Loading...' : isFollowing ? '✓ Followed' : '+ Follow Organizer'}
                                        </button>
                                    </div>

                                    <p className="text-center text-xs text-slate-500 mt-3">
                                        One-click registration powered by InfiniteBZ
                                    </p>

                                </div>
                                <div className="flex items-start gap-4">
                                    <div className="p-3 rounded-lg bg-slate-800 text-purple-500 border border-slate-700">
                                        <MapPin size={24} />
                                    </div>
                                    <div>
                                        <p className="text-sm text-slate-400 font-medium uppercase tracking-wide mb-1">Location</p>
                                        <p className="text-white font-bold text-lg">
                                            {event.venue_name || "Online"}
                                        </p>
                                        <p className="text-slate-400">
                                            {event.venue_address || "Link available after registration"}
                                        </p>
                                    </div>


                                    {/* Mini Map Placeholder */}
                                    <div className="h-32 bg-slate-700/30 rounded-xl w-full relative overflow-hidden group cursor-pointer">
                                        <div className="absolute inset-0 bg-[url('https://api.mapbox.com/styles/v1/mapbox/dark-v10/static/80.2376,13.0674,13,0/300x200?access_token=PLACEHOLDER')] bg-cover opacity-50 grayscale group-hover:grayscale-0 transition-all" />
                                        <div className="absolute inset-0 flex items-center justify-center">
                                            <div className="bg-white text-slate-900 px-3 py-1.5 rounded-lg shadow-lg text-xs font-bold flex items-center gap-1 group-hover:scale-110 transition-transform">
                                                <MapPin size={12} className="text-red-500" /> View Map
                                            </div>
                                        </div>
                                    </div>
                                </div>

                                {/* ORGANIZER CARD */}
                                <div className="bg-slate-800/50 rounded-2xl p-6 border border-slate-700/50 flex items-center gap-4">
                                    <div className="w-12 h-12 rounded-full bg-gradient-to-br from-primary-500 to-purple-600 flex items-center justify-center text-white font-bold text-lg">
                                        {event.organizer_name?.[0] || 'C'}
                                    </div>
                                    <div className="flex-1">
                                        <p className="font-bold text-white text-sm">{event.organizer_name || "Community Host"}</p>
                                        <p className="text-xs text-slate-400">Organized by {event.organizer_name?.split(' ')[0]}</p>
                                    </div>

                                </div>
                            </div>

                            {/* TABS & CONTENT */}
                            <div>
                                <div className="flex gap-8 border-b border-slate-800 mb-8 overflow-x-auto">
                                    {['About', 'Agenda', 'Speakers'].map((tab) => (
                                        <button
                                            key={tab}
                                            onClick={() => setActiveTab(tab.toLowerCase())}
                                            className={`pb-4 text-sm font-bold uppercase tracking-wider transition-all whitespace-nowrap ${activeTab === tab.toLowerCase()
                                                ? 'text-primary-500 border-b-2 border-primary-500'
                                                : 'text-slate-500 hover:text-slate-300'
                                                }`}
                                        >
                                            {tab}
                                        </button>
                                    ))}
                                </div>

                                <div className="animate-in fade-in slide-in-from-bottom-4 duration-500">
                                    {activeTab === 'about' && (
                                        <div className="prose prose-invert max-w-none">
                                            <p className="text-slate-300 text-lg leading-relaxed whitespace-pre-wrap">
                                                {event.description || "Join us for an immersive experience designed to connect, educate, and inspire. This event brings together the brightest minds in the industry."}
                                            </p>

                                            <div className="mt-8 grid grid-cols-1 md:grid-cols-2 gap-4">
                                                {[
                                                    "Networking sessions", "Expert Panels", "Q&A Rounds", "Certificate"
                                                ].map((perk, i) => (
                                                    <div key={i} className="flex items-center gap-3 p-4 bg-slate-800/30 rounded-xl border border-white/5">
                                                        <CheckCircle2 className="text-green-500" size={20} />
                                                        <span className="text-slate-200 font-medium">{perk}</span>
                                                    </div>
                                                ))}
                                            </div>
                                        </div>
                                    )}

                                    {activeTab === 'agenda' && (
                                        <div className="space-y-6 relative border-l-2 border-slate-800 ml-4 pl-8">
                                            {agenda.map((item, i) => (
                                                <div key={i} className="relative">
                                                    <div className="absolute -left-[39px] top-1 h-5 w-5 rounded-full bg-slate-900 border-4 border-slate-700" />
                                                    <p className="text-sm font-bold text-primary-500 mb-1">{item.time}</p>
                                                    <h4 className="text-xl font-bold text-white mb-2">{item.title}</h4>
                                                    <p className="text-slate-400 text-base">{item.desc}</p>
                                                </div>
                                            ))}
                                        </div>
                                    )}

                                    {activeTab === 'speakers' && (
                                        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                                            {speakers.map((speaker, i) => (
                                                <div key={i} className="flex items-center gap-5 p-5 bg-slate-800/40 rounded-2xl border border-white/5 hover:bg-slate-800/60 transition-colors">
                                                    <img src={speaker.image} className="w-16 h-16 rounded-full object-cover ring-2 ring-slate-700" />
                                                    <div>
                                                        <h4 className="text-lg font-bold text-white">{speaker.name}</h4>
                                                        <p className="text-sm text-primary-400 mb-2">{speaker.role}</p>
                                                        <div className="flex gap-3 text-slate-500">
                                                            <Linkedin size={16} className="hover:text-white cursor-pointer" />
                                                            <Twitter size={16} className="hover:text-white cursor-pointer" />
                                                        </div>
                                                    </div>
                                                </div>
                                            ))}
                                        </div>
                                    )}
                                </div>
                            </div>

                            {/* REGISTRATION FOOTER/CARD */}
                            <div className="sticky bottom-0 bg-slate-900/95 backdrop-blur-xl border-t border-slate-800 -mx-8 -mb-8 p-8 flex items-center justify-between gap-6 lg:static lg:bg-transparent lg:border-none lg:p-0 lg:m-0 lg:mt-12">
                                <div>
                                    <p className="text-slate-400 text-sm mb-1 uppercase tracking-wide font-bold">Total Price</p>
                                    <div className="flex items-baseline gap-2">
                                        <span className="text-4xl font-black text-white">
                                            {event.is_free ? 'Free' : `₹${event.raw_data?.price || 499}`}
                                        </span>
                                        {!event.is_free && <span className="text-slate-500 line-through">₹999</span>}
                                    </div>
                                </div>

                                <button
                                    onClick={() => !isRegistered && onRegister(event)}
                                    disabled={isRegistered}
                                    className={`px-10 py-4 rounded-xl font-bold text-lg flex items-center gap-3 transition-all transform hover:-translate-y-1 ${isRegistered
                                        ? 'bg-green-500/20 text-green-400 cursor-default'
                                        : 'bg-primary-600 hover:bg-primary-500 text-white shadow-xl shadow-primary-600/20'
                                        }`}
                                >
                                    {isRegistered ? (
                                        <> <CheckCircle2 /> Registered </>
                                    ) : (
                                        <> <Ticket className="animate-pulse" /> Confirm Registration </>
                                    )}
                                </button>
                            </div>

                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}
