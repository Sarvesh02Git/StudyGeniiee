import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';

@Component({
  selector: 'app-upload',
  standalone: true,
  imports: [CommonModule, MatButtonModule, MatIconModule],
  templateUrl: './upload.html',
  styleUrls: ['./upload.css']
})
export class UploadComponent {
  uploadedFileName: string | null = null;
  filePreview: string | null = null;

  onFileSelected(event: Event) {
    const input = event.target as HTMLInputElement;
    if (input.files && input.files[0]) {
      const file = input.files[0];
      this.uploadedFileName = file.name;

      if (file.type === 'application/pdf') {
        this.filePreview = 'PDF file selected – preview not available here.';
      } else if (file.type.startsWith('image/')) {
        const reader = new FileReader();
        reader.onload = e => this.filePreview = e.target?.result as string;
        reader.readAsDataURL(file);
      } else {
        this.filePreview = 'Unsupported file format.';
      }
    }
  }

  generateSummary() {
    alert('📑 Generating summary... (API integration pending)');
  }

  generateQuiz() {
    alert('📝 Generating quiz... (API integration pending)');
  }

  generateFlashcards() {
    alert('🎴 Generating flashcards... (API integration pending)');
  }
}
