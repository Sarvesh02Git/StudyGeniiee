import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { MatButtonModule } from '@angular/material/button';
import { RouterModule } from '@angular/router';

// If you want a navbar here, you can also import Angular Material buttons, etc.

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, MatButtonModule,  RouterModule],
  templateUrl: './app.html',
  styleUrls: ['./app.css']
})
export class App{
  title = 'StudyGenie';
}
