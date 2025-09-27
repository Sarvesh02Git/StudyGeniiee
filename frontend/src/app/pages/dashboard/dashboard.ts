import { Component, OnInit } from '@angular/core';
import { CommonModule, DecimalPipe } from '@angular/common'; // <--- Import CommonModule and DecimalPipe
import { ApiService } from '../../services/api';
import { RouterModule } from '@angular/router'; // Keep RouterModule if you plan to add routerLink later, or remove if not needed.

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [CommonModule, DecimalPipe, RouterModule], // <--- Add CommonModule, DecimalPipe, RouterModule
  templateUrl: './dashboard.html',
  styleUrls: ['./dashboard.css']
})
export class DashboardComponent implements OnInit {
  // Declare properties used in the template
  userProgress: {
    study_streak?: number;
    quizzes_completed?: number;
    average_score?: number;
    total_flashcards_reviewed?: number;
  } | null = null; // Initialize userProgress to null or an empty object
  
  loading = true; // Initialize loading state
  error: string | null = null; // Initialize error state

  // This should come from an authentication service in a real app
  dummyUserId: number = 1; 

  constructor(private apiService: ApiService) { }

  ngOnInit(): void {
    this.fetchUserProgress();
  }

  fetchUserProgress(): void {
    this.loading = true;
    this.error = null;
    this.apiService.getUserProgress(this.dummyUserId).subscribe({
      next: (data) => {
        this.userProgress = {
          study_streak: data.study_streak || 0,
          quizzes_completed: data.quizzes_completed || 0,
          average_score: data.average_score || 0,
          total_flashcards_reviewed: data.total_flashcards_reviewed || 0
        };
        this.loading = false;
        console.log('User progress', data);
      },
      error: (err) => {
        this.error = err.error?.detail || 'Failed to fetch user progress.';
        this.loading = false;
        console.error('Error fetching user progress', err);
      }
    });
  }
}
