import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';
import { Route } from '@angular/router';
//import { RouterOutlet } from '@angular/router';
import { RouterLinkActive } from '@angular/router';

@Component({
  selector: 'app-navbar',
  imports : [RouterLink,RouterLinkActive],
  standalone: true,
  templateUrl: './navbar.html',
  styleUrls: ['./navbar.css']
})
export class NavbarComponent {}
