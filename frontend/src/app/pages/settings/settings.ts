import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { MatCardModule } from '@angular/material/card';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatSlideToggleModule } from '@angular/material/slide-toggle';
import { MatButtonModule } from '@angular/material/button';

@Component({
  selector: 'app-settings',
  standalone: true,
  templateUrl: './settings.html',
  styleUrls: ['./settings.css'],
  imports: [
    FormsModule,
    MatCardModule,
    MatFormFieldModule,
    MatInputModule,
    MatSlideToggleModule,
    MatButtonModule
  ]
})
export class SettingsComponent {
  username: string = '';
  email: string = '';
  darkMode: boolean = false;
  notifications: boolean = true;
  

  toggleDarkMode() {
    this.darkMode = !this.darkMode;
    document.body.classList.toggle('dark-theme', this.darkMode);
  }

  saveSettings() {
    console.log('Settings saved:', {
      darkMode: this.darkMode,
      notifications: this.notifications,
      username: this.username,
      email: this.email
    });
    alert('Settings saved successfully!');
  }
}
