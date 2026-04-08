# environment.py
from pydantic import BaseModel
from typing import Optional, Dict, List, Any
import random
from data.emails import EMAILS_DATABASE

class Observation(BaseModel):
    email_text: str
    current_step: int
    total_emails: int
    current_score: float
    max_possible_score: float

class Action(BaseModel):
    category: str
    urgency: Optional[str] = None
    department: Optional[str] = None

class EmailTriageEnvironment:
    def __init__(self, task_level="easy"):
        self.task_level = task_level
        self.emails = []
        self.current_index = 0
        self.total_score = 0
        self.max_score = 0
        
        if task_level == "easy":
            self.emails = [e for e in EMAILS_DATABASE if e['difficulty'] == 'easy'][:4]
            self.max_score = 4.0
        elif task_level == "medium":
            self.emails = [e for e in EMAILS_DATABASE if e['difficulty'] in ['easy', 'medium']][:5]
            self.max_score = 4.0
        else:
            self.emails = EMAILS_DATABASE[:6]
            self.max_score = 6.0
    
    def reset(self):
        random.shuffle(self.emails)
        self.current_index = 0
        self.total_score = 0
        return self._get_observation()
    
    def step(self, action: Action):
        if self.current_index >= len(self.emails):
            return self._get_observation(), 0, True, {"message": "Done"}
        
        current_email = self.emails[self.current_index]
        reward = self._calculate_reward(action, current_email)
        self.total_score += reward
        
        self.current_index += 1
        done = self.current_index >= len(self.emails)
        
        obs = self._get_observation()
        return obs, reward, done, {"correct_answer": current_email['correct_category']}
    
    def _calculate_reward(self, action: Action, email: Dict) -> float:
        if self.task_level == "easy":
            return 1.0 if action.category == email['correct_category'] else 0.0
        
        elif self.task_level == "medium":
            score = 0.0
            if action.category == email['correct_category']:
                score += 0.6
            if action.urgency == email.get('urgency', 'normal'):
                score += 0.2
            return score
        
        else:
            score = 0.0
            if action.category == email['correct_category']:
                score += 0.6
            if action.urgency == email.get('urgency', 'normal'):
                score += 0.2
            if action.department == email.get('department', 'general'):
                score += 0.2
            return score
    
    def _get_observation(self):
        if self.current_index >= len(self.emails):
            return Observation(
                email_text="DONE",
                current_step=self.current_index,
                total_emails=len(self.emails),
                current_score=self.total_score,
                max_possible_score=self.max_score
            )
        
        email = self.emails[self.current_index]
        email_text = f"From: {email['from']}\nSubject: {email['subject']}\nBody: {email['body']}"
        return Observation(
            email_text=email_text,
            current_step=self.current_index,
            total_emails=len(self.emails),
            current_score=self.total_score,
            max_possible_score=self.max_score
        )
    
    def state(self):
        return {
            "task": self.task_level,
            "progress": f"{self.current_index}/{len(self.emails)}",
            "current_score": self.total_score,
            "max_score": self.max_score,
            "percentage": (self.total_score / self.max_score * 100) if self.max_score > 0 else 0
        }