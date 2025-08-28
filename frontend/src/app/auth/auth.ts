import { Component, signal } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ReactiveFormsModule, FormBuilder, Validators } from '@angular/forms';
import { Router, RouterLink } from '@angular/router'; // Import Router

@Component({
  selector: 'app-auth',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule, RouterLink],
  templateUrl: './auth.html',
  styleUrls: ['./auth.css'],
})
export class Auth {
  // state: true => Register screen, false => Login screen
  isRegister = signal(false);

  loginForm;
  registerForm;

  constructor(private fb: FormBuilder, private router: Router) { // Inject Router
    this.loginForm = this.fb.group({
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required, Validators.minLength(6)]],
    });

    this.registerForm = this.fb.group({
      name: ['', [Validators.required, Validators.minLength(2)]],
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required, Validators.minLength(6)]],
    });
  }

  toggle(mode: 'login' | 'register') {
    this.isRegister.set(mode === 'register');
  }

  submitLogin() {
    if (this.loginForm.invalid) {
      this.loginForm.markAllAsTouched();
      return;
    }
    console.log('LOGIN =>', this.loginForm.value);
    // Simulate successful login and navigate
    alert('Login successful!');
    this.router.navigateByUrl('/dashboard'); 
  }

  submitRegister() {
    if (this.registerForm.invalid) {
      this.registerForm.markAllAsTouched();
      return;
    }
    console.log('REGISTER =>', this.registerForm.value);
    // Simulate successful registration, then switch to login
    alert('Registration successful! Please log in.');
    this.toggle('login');
  }
}
