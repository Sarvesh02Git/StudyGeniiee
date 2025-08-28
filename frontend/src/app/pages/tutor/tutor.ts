import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatCardModule } from '@angular/material/card';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';

interface Session {
  date: string;
  time: string;
  topic: string;
}

@Component({
  selector: 'app-tutor',
  standalone: true,
  imports: [CommonModule, MatCardModule, MatButtonModule, MatIconModule],
  templateUrl: './tutor.html',
  styleUrls: ['./tutor.css']
})
export class TutorComponent {
  tutor = {
    name: 'Dr. Sarah Johnson',
    subject: 'Computer Science',
    rating: 4.8,
    description: 'Experienced tutor specializing in Web Development, Angular, and AI-based applications.'
  };

  sessions: Session[] = [
    { date: 'Aug 25, 2025', time: '10:00 AM', topic: 'Introduction to Angular' },
    { date: 'Aug 27, 2025', time: '2:00 PM', topic: 'RxJS and Observables' },
    { date: 'Aug 29, 2025', time: '6:00 PM', topic: 'State Management in Angular' }
  ];

  bookSession(session: Session) {
    alert(`You booked: ${session.topic} on ${session.date} at ${session.time}`);
  }
}
