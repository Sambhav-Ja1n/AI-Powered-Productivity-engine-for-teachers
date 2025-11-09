"""
Feature 4: AI-Powered Scheduling & Intelligent Reward System
AI analyzes schedules for conflicts, suggests optimal times, and personalizes rewards
"""

import os
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import json
from pathlib import Path
from groq import Groq

class SchedulingRewardSystem:
    def __init__(self, groq_api_key: str, data_dir: str = "data", model: str = "llama-3.3-70b-versatile"):
        """Initialize AI-powered scheduling and reward system"""
        self.client = Groq(api_key=groq_api_key)
        self.model = model
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(exist_ok=True)
        
        self.schedule_file = self.data_dir / "schedule.json"
        self.rewards_file = self.data_dir / "rewards.json"
        
        self.schedule = self._load_schedule()
        self.rewards = self._load_rewards()
    
    def _load_schedule(self) -> Dict:
        """Load schedule from JSON file"""
        if self.schedule_file.exists():
            with open(self.schedule_file, 'r') as f:
                return json.load(f)
        return {
            "classes": [],
            "assignments": [],
            "events": []
        }
    
    def _save_schedule(self):
        """Save schedule to JSON file"""
        with open(self.schedule_file, 'w') as f:
            json.dump(self.schedule, f, indent=2)
    
    def _load_rewards(self) -> Dict:
        """Load rewards data from JSON file"""
        if self.rewards_file.exists():
            with open(self.rewards_file, 'r') as f:
                return json.load(f)
        return {
            "teachers": {},
            "students": {},
            "badges": self._get_default_badges()
        }
    
    def _save_rewards(self):
        """Save rewards to JSON file"""
        with open(self.rewards_file, 'w') as f:
            json.dump(self.rewards, f, indent=2)
    
    def _get_default_badges(self) -> List[Dict]:
        """Define available badges"""
        return [
            {
                "id": "early_bird",
                "name": "Early Bird",
                "description": "Submitted 5 assignments before deadline",
                "icon": "🌅",
                "points_required": 0,
                "criteria": "early_submissions >= 5"
            },
            {
                "id": "consistent_learner",
                "name": "Consistent Learner",
                "description": "Completed assignments for 10 consecutive days",
                "icon": "📚",
                "points_required": 0,
                "criteria": "consecutive_days >= 10"
            },
            {
                "id": "excellence",
                "name": "Excellence Award",
                "description": "Scored above 90% on 5 assignments",
                "icon": "⭐",
                "points_required": 0,
                "criteria": "high_scores >= 5"
            },
            {
                "id": "dedicated_teacher",
                "name": "Dedicated Teacher",
                "description": "Graded 50+ assignments",
                "icon": "👨‍🏫",
                "points_required": 0,
                "criteria": "graded_count >= 50"
            },
            {
                "id": "innovator",
                "name": "Teaching Innovator",
                "description": "Created 10+ custom learning materials",
                "icon": "💡",
                "points_required": 0,
                "criteria": "materials_created >= 10"
            },
            {
                "id": "point_master",
                "name": "Point Master",
                "description": "Earned 1000 points",
                "icon": "🏆",
                "points_required": 1000,
                "criteria": "total_points >= 1000"
            }
        ]
    
    # === SCHEDULING FEATURES ===
    
    def add_class(self, class_data: Dict) -> str:
        """Add a class to schedule
        
        class_data should contain:
        - name: str
        - day: str (Monday, Tuesday, etc.)
        - start_time: str (HH:MM)
        - end_time: str (HH:MM)
        - subject: str
        - room: str (optional)
        """
        class_id = f"class_{len(self.schedule['classes']) + 1}"
        class_entry = {
            "id": class_id,
            "created_at": datetime.now().isoformat(),
            **class_data
        }
        self.schedule['classes'].append(class_entry)
        self._save_schedule()
        return class_id
    
    def add_assignment(self, assignment_data: Dict) -> str:
        """Add assignment with deadline
        
        assignment_data should contain:
        - title: str
        - subject: str
        - due_date: str (YYYY-MM-DD)
        - description: str (optional)
        - points: int (for reward system)
        """
        assignment_id = f"assign_{len(self.schedule['assignments']) + 1}"
        assignment_entry = {
            "id": assignment_id,
            "created_at": datetime.now().isoformat(),
            "status": "pending",
            **assignment_data
        }
        self.schedule['assignments'].append(assignment_entry)
        self._save_schedule()
        return assignment_id
    
    def get_upcoming_schedule(self, days: int = 7) -> Dict:
        """Get schedule for next N days"""
        today = datetime.now().date()
        end_date = today + timedelta(days=days)
        
        upcoming_assignments = []
        for assignment in self.schedule['assignments']:
            try:
                due_date = datetime.fromisoformat(assignment['due_date']).date()
                if today <= due_date <= end_date and assignment['status'] == 'pending':
                    days_until = (due_date - today).days
                    assignment_copy = assignment.copy()
                    assignment_copy['days_until_due'] = days_until
                    upcoming_assignments.append(assignment_copy)
            except:
                pass
        
        # Sort by due date
        upcoming_assignments.sort(key=lambda x: x.get('due_date', ''))
        
        return {
            "period": f"Next {days} days",
            "start_date": today.isoformat(),
            "end_date": end_date.isoformat(),
            "assignments": upcoming_assignments,
            "total_pending": len(upcoming_assignments)
        }
    
    def get_todays_classes(self) -> List[Dict]:
        """Get today's class schedule"""
        today = datetime.now().strftime("%A")  # e.g., "Monday"
        
        todays_classes = [
            c for c in self.schedule['classes']
            if c.get('day', '').lower() == today.lower()
        ]
        
        # Sort by start time
        todays_classes.sort(key=lambda x: x.get('start_time', ''))
        
        return todays_classes
    
    def mark_assignment_complete(self, assignment_id: str, user_id: str, 
                                 user_type: str = "student", score: int = 100):
        """Mark assignment as complete and award points"""
        for assignment in self.schedule['assignments']:
            if assignment['id'] == assignment_id:
                assignment['status'] = 'completed'
                assignment['completed_at'] = datetime.now().isoformat()
                assignment['completed_by'] = user_id
                
                # Award points
                points = assignment.get('points', 10)
                self.add_points(user_id, points, user_type, f"Completed {assignment['title']}")
                
                # Bonus for early submission
                try:
                    due_date = datetime.fromisoformat(assignment['due_date']).date()
                    if datetime.now().date() < due_date:
                        self.add_points(user_id, 5, user_type, "Early submission bonus")
                except:
                    pass
                
                self._save_schedule()
                return True
        return False
    
    # === REWARD SYSTEM ===
    
    def add_points(self, user_id: str, points: int, user_type: str = "student", 
                   reason: str = "") -> Dict:
        """Add points to user"""
        if user_type not in self.rewards:
            self.rewards[user_type + "s"] = {}
        
        user_key = user_type + "s"
        
        if user_id not in self.rewards[user_key]:
            self.rewards[user_key][user_id] = {
                "name": user_id,
                "total_points": 0,
                "badges": [],
                "history": [],
                "stats": {
                    "early_submissions": 0,
                    "consecutive_days": 0,
                    "high_scores": 0,
                    "graded_count": 0,
                    "materials_created": 0
                }
            }
        
        user_data = self.rewards[user_key][user_id]
        user_data['total_points'] += points
        user_data['history'].append({
            "timestamp": datetime.now().isoformat(),
            "points": points,
            "reason": reason
        })
        
        # Check for new badges
        new_badges = self._check_badges(user_data)
        
        self._save_rewards()
        
        return {
            "user_id": user_id,
            "points_added": points,
            "total_points": user_data['total_points'],
            "new_badges": new_badges
        }
    
    def _check_badges(self, user_data: Dict) -> List[str]:
        """Check if user earned new badges"""
        new_badges = []
        current_badges = user_data.get('badges', [])
        stats = user_data.get('stats', {})
        total_points = user_data.get('total_points', 0)
        
        for badge in self.rewards['badges']:
            badge_id = badge['id']
            
            # Skip if already earned
            if badge_id in current_badges:
                continue
            
            # Check points requirement
            if badge['points_required'] > 0:
                if total_points >= badge['points_required']:
                    user_data['badges'].append(badge_id)
                    new_badges.append(badge)
            
            # Check criteria (simplified evaluation)
            criteria = badge.get('criteria', '')
            try:
                # Simple evaluation of criteria
                if eval(criteria.format(**stats)):
                    user_data['badges'].append(badge_id)
                    new_badges.append(badge)
            except:
                pass
        
        return new_badges
    
    def get_leaderboard(self, user_type: str = "student", top_n: int = 10) -> List[Dict]:
        """Get top users by points"""
        user_key = user_type + "s"
        
        if user_key not in self.rewards or not self.rewards[user_key]:
            return []
        
        users = []
        for user_id, data in self.rewards[user_key].items():
            users.append({
                "user_id": user_id,
                "name": data.get('name', user_id),
                "total_points": data.get('total_points', 0),
                "badge_count": len(data.get('badges', []))
            })
        
        # Sort by points
        users.sort(key=lambda x: x['total_points'], reverse=True)
        
        return users[:top_n]
    
    def get_user_profile(self, user_id: str, user_type: str = "student") -> Dict:
        """Get user's complete profile with points, badges, and progress"""
        user_key = user_type + "s"
        
        if user_key not in self.rewards or user_id not in self.rewards[user_key]:
            return {
                "user_id": user_id,
                "total_points": 0,
                "badges": [],
                "badge_count": 0,
                "rank": None,
                "message": "User not found"
            }
        
        user_data = self.rewards[user_key][user_id]
        
        # Get rank
        leaderboard = self.get_leaderboard(user_type, top_n=1000)
        rank = next((i + 1 for i, u in enumerate(leaderboard) if u['user_id'] == user_id), None)
        
        # Get badge details
        user_badge_ids = user_data.get('badges', [])
        earned_badges = [b for b in self.rewards['badges'] if b['id'] in user_badge_ids]
        
        return {
            "user_id": user_id,
            "name": user_data.get('name', user_id),
            "total_points": user_data.get('total_points', 0),
            "badges": earned_badges,
            "badge_count": len(earned_badges),
            "rank": rank,
            "recent_activity": user_data.get('history', [])[-5:]
        }
    
    # === AI-POWERED FEATURES ===
    
    def ai_analyze_schedule_conflicts(self) -> Dict:
        """Use AI to detect scheduling conflicts and suggest optimizations"""
        classes_summary = []
        for cls in self.schedule['classes']:
            classes_summary.append(f"{cls['day']} {cls['start_time']}-{cls['end_time']}: {cls['name']} ({cls['subject']})")
        
        assignments_summary = []
        for assign in self.schedule['assignments']:
            if assign['status'] == 'pending':
                assignments_summary.append(f"{assign['due_date']}: {assign['title']} ({assign['subject']})")
        
        prompt = f"""Analyze this teacher's schedule for conflicts and workload balance:

CLASSES:
{chr(10).join(classes_summary) if classes_summary else 'No classes scheduled'}

PENDING ASSIGNMENTS:
{chr(10).join(assignments_summary[:10]) if assignments_summary else 'No pending assignments'}

Provide:
1. Any time conflicts or overlapping classes
2. Days with heavy workload
3. Suggestions for better workload distribution
4. Warning about deadline clusters
5. Recommended break times

Format as a numbered list."""
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are an AI scheduling assistant that helps teachers optimize their schedules. Provide clear, actionable insights."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=800
            )
            
            analysis = response.choices[0].message.content
            
            return {
                "status": "success",
                "analysis": analysis.replace('\n', '<br>'),
                "total_classes": len(self.schedule['classes']),
                "pending_assignments": len([a for a in self.schedule['assignments'] if a['status'] == 'pending'])
            }
        except Exception as e:
            return {
                "status": "error",
                "analysis": f"Error analyzing schedule: {str(e)}"
            }
    
    def ai_suggest_optimal_time(self, subject: str, duration_minutes: int = 60) -> Dict:
        """AI suggests best time to schedule a new class based on existing schedule"""
        classes_by_day = {}
        for cls in self.schedule['classes']:
            day = cls['day']
            if day not in classes_by_day:
                classes_by_day[day] = []
            classes_by_day[day].append(f"{cls['start_time']}-{cls['end_time']}: {cls['name']}")
        
        schedule_summary = "\n".join([
            f"{day}: {', '.join(times) if times else 'Free'}"
            for day, times in classes_by_day.items()
        ])
        
        prompt = f"""I need to schedule a new {subject} class that's {duration_minutes} minutes long.

Current weekly schedule:
{schedule_summary if schedule_summary else 'No classes scheduled yet'}

Suggest:
1. Best day of the week
2. Optimal time slot (start and end time)
3. Reasoning based on workload distribution and pedagogical best practices
4. Alternative options

Consider: avoiding back-to-back classes, energy levels throughout the day, and balanced weekly distribution."""
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are an AI scheduling expert for educators. Suggest optimal times based on cognitive science and work-life balance principles."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=500
            )
            
            suggestion = response.choices[0].message.content
            
            return {
                "status": "success",
                "suggestion": suggestion.replace('\n', '<br>'),
                "subject": subject,
                "duration": duration_minutes
            }
        except Exception as e:
            return {
                "status": "error",
                "suggestion": f"Error generating suggestion: {str(e)}"
            }
    
    def ai_personalized_reward_suggestions(self, user_id: str, user_type: str = "student") -> Dict:
        """AI analyzes user performance and suggests personalized rewards/motivations"""
        profile = self.get_user_profile(user_id, user_type)
        
        if profile.get('message') == 'User not found':
            # Create user profile
            self.add_points(user_id, 0, user_type, "Profile created")
            profile = self.get_user_profile(user_id, user_type)
        
        badges_earned = len(profile.get('badges', []))
        total_points = profile.get('total_points', 0)
        recent_activity = profile.get('recent_activity', [])
        
        activity_summary = "\n".join([
            f"{act['reason']}: +{act['points']} points"
            for act in recent_activity[-5:]
        ]) if recent_activity else "No recent activity"
        
        prompt = f"""Analyze this {user_type}'s performance and suggest personalized rewards/motivation:

USER: {user_id}
Total Points: {total_points}
Badges Earned: {badges_earned}

Recent Activity:
{activity_summary}

Provide:
1. Personalized encouragement based on their progress
2. Next achievable badge or milestone to aim for
3. Specific actions they can take to earn more points
4. Motivational message tailored to their activity pattern

Be encouraging and specific!"""
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a motivational AI coach for students and teachers. Provide personalized, encouraging feedback."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.8,
                max_tokens=600
            )
            
            recommendations = response.choices[0].message.content
            
            return {
                "status": "success",
                "user_id": user_id,
                "recommendations": recommendations.replace('\n', '<br>'),
                "current_points": total_points,
                "badges_count": badges_earned
            }
        except Exception as e:
            return {
                "status": "error",
                "recommendations": f"Error generating recommendations: {str(e)}"
            }


if __name__ == "__main__":
    # Test scheduling and rewards
    system = SchedulingRewardSystem()
    
    # Add sample class
    class_id = system.add_class({
        "name": "Mathematics 101",
        "day": "Monday",
        "start_time": "09:00",
        "end_time": "10:30",
        "subject": "Mathematics",
        "room": "Room 101"
    })
    print(f"Added class: {class_id}")
    
    # Add sample assignment
    assignment_id = system.add_assignment({
        "title": "Algebra Homework",
        "subject": "Mathematics",
        "due_date": (datetime.now() + timedelta(days=3)).date().isoformat(),
        "description": "Complete exercises 1-10",
        "points": 20
    })
    print(f"Added assignment: {assignment_id}")
    
    # Test rewards
    result = system.add_points("student_123", 50, "student", "Test points")
    print(f"Points added: {result}")
