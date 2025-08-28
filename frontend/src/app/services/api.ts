import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private baseUrl = 'http://127.0.0.1:8000/api'; // FastAPI backend URL

  constructor(private http: HttpClient) {}
  
  login(credentials: { email: string; password: string }): Observable<any> {
    return this.http.post(`${this.baseUrl}/login`, credentials);
  }

  
  register(data: { email: string; password: string }): Observable<any> {
    return this.http.post(`${this.baseUrl}/register`, data);
  }

  getQuizzes(): Observable<any> {
    return this.http.get(`${this.baseUrl}/quizzes`);
  }

  submitQuiz(answers: any): Observable<any> {
    return this.http.post(`${this.baseUrl}/submit`, answers);
  }
}
