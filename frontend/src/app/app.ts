// src/app/app.ts
import { Component } from '@angular/core';
import { RouterOutlet, RouterModule } from '@angular/router';
//import { NavbarComponent } from './navbar/navbar'; // <--- This path should be correct if navbar.component.ts is directly inside src/app/navbar/

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, RouterModule], 
  templateUrl: './app.html',
  styleUrls: ['./app.css'] 
})
export class App {
  title = 'StudyGenie';
}
