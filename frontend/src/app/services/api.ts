import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, of } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private baseUrl = 'http://127.0.0.1:8000/api'; // FastAPI backend URL

  constructor(private http: HttpClient) {}
  
  getUserProgress(userId: number): Observable<any> {
    // Replace this mock implementation with a real HTTP request as needed
    return of({
      study_streak: 5,
      quizzes_completed: 12,
      average_score: 88,
      total_flashcards_reviewed: 150
    });
  }


  login(credentials: { email: string; password: string }): Observable<any> {
    return this.http.post(`${this.baseUrl}/auth/login`, credentials);
  }

  
  register(data: { email: string; password: string }): Observable<any> {
    return this.http.post(`${this.baseUrl}/auth/register`, data);
  }

  forgotPassword(email: string): Observable<any> {
    return this.http.post(`${this.baseUrl}/auth/forgot-password`, { email });
  }

  resetPassword(token: string, newPassword: string): Observable<any> {
    return this.http.post(`${this.baseUrl}/auth/reset-password/${token}`, { new_password: newPassword });
  }

  getQuizzes(): Observable<any> {
    return this.http.get(`${this.baseUrl}/quizzes`);
  }

  submitQuiz(answers: any): Observable<any> {
    return this.http.post(`${this.baseUrl}/submit`, answers);
  }
}
