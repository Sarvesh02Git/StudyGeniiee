import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
// No longer needs to import NavbarComponent as it's in app.html
// import { NavbarComponent } from '../navbar/navbar.component';
// import { NavbarComponent } from '../navbar/navbar';

@Component({
  selector: 'app-main-layout',
  standalone: true,
  imports: [RouterOutlet],
  templateUrl: './main-layout.html',
  styleUrls: ['./main-layout.css'] // You'll need to define main-layout.css
})
export class MainLayoutComponent {}
