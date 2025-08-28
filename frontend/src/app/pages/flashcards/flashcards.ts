import { Component } from '@angular/core';
import { NgFor } from '@angular/common';

@Component({
  selector: 'app-flashcards',
  imports : [NgFor],
  templateUrl: './flashcards.html',
  styleUrls: ['./flashcards.css']
})
export class FlashcardsComponent {
  flashcards = [
    { question: 'What is the capital of France?', answer: 'Paris', flipped: false },
    { question: 'Who developed Angular?', answer: 'Google', flipped: false },
    { question: 'What does HTML stand for?', answer: 'HyperText Markup Language', flipped: false },
    { question: 'What is the speed of light?', answer: '299,792 km/s', flipped: false }
  ];

  toggleCard(card: any) {
    card.flipped = !card.flipped;
  }
}
