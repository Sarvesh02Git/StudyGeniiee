import { Component } from '@angular/core';
import { CommonModule } from '@angular/common'; // 👈 Add this
import { MatCardModule } from '@angular/material/card'; // 👈 For mat-card
import { MatButtonModule } from '@angular/material/button'; // 👈 For mat-button

@Component({
  selector: 'app-quizzes',
  standalone: true, // 👈 important if you’re using standalone
  imports: [CommonModule, MatCardModule, MatButtonModule], // 👈 add imports here
  templateUrl: './quizzes.html',
  styleUrls: ['./quizzes.css']
})
export class QuizzesComponent {
  quizzes = [
    {
      question: 'What is Angular?',
      options: ['Framework', 'Library', 'Language', 'IDE'],
      correctAnswer: 0,
      selectedAnswer: null as number | null // 👈 make it number|null
    },
    {
      question: 'TypeScript is a superset of?',
      options: ['Python', 'Java', 'JavaScript', 'C#'],
      correctAnswer: 2,
      selectedAnswer: null as number | null
    }
  ];

  score: number | null = null;

  selectAnswer(questionIndex: number, optionIndex: number) {
    this.quizzes[questionIndex].selectedAnswer = optionIndex;
  }

  submitQuiz() {
    let total = 0;
    this.quizzes.forEach(q => {
      if (q.selectedAnswer === q.correctAnswer) {
        total++;
      }
    });
    this.score = total;
  }

  resetQuiz() {
    this.quizzes.forEach(q => (q.selectedAnswer = null));
    this.score = null;
  }
}
