import { Component, OnInit } from '@angular/core';
import { MatProgressBarModule } from '@angular/material/progress-bar';
import { MatCardModule } from '@angular/material/card';
import { MatButtonModule } from '@angular/material/button';
import { RouterLink, RouterModule } from '@angular/router';
import { routes } from '../../app.routes';

@Component({
  selector: 'app-dashboard',
  imports: [MatProgressBarModule, MatButtonModule, MatCardModule, RouterLink, RouterModule ],
  templateUrl: './dashboard.html',
  styleUrls: ['./dashboard.css']
})
export class DashboardComponent implements OnInit {

  // Example data – in real app this will come from backend API
  progressValue: number = 70;       // Knowledge coverage %
  studyStreak: number = 5;          // Consecutive study days
  totalFlashcards: number = 120;    // Total flashcards reviewed
  completedQuizzes: number = 8;     // Completed quizzes
  lastStudyDate: string = '';       // Last study session date

  constructor() {}

  ngOnInit(): void {
    // Simulate fetching data (this will be replaced with API call later)
    this.loadDashboardData();
  }

  loadDashboardData() {
    const today = new Date();
    this.lastStudyDate = today.toDateString();

    // Example: you could also pull user data from local storage
    // or call a service: this.dashboardService.getUserStats()
  }

  // Example action handler
  startNewQuiz() {
    alert('Redirecting to new quiz page...');
  }
}
