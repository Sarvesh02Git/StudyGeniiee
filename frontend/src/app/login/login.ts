import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { Router, RouterModule } from '@angular/router';
import { HttpClientModule } from '@angular/common/http'; // <--- ADD THIS IMPORT
import { ApiService } from '../services/api';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule, RouterModule, HttpClientModule], // <--- ADD HttpClientModule here
  templateUrl: './login.html',
  styleUrls: ['./login.css']
})
export class Login implements OnInit {
  loginForm: FormGroup;
  isLoading = false;
  error: string | null = null;

  constructor(
    private fb: FormBuilder,
    private apiService: ApiService,
    private router: Router
  ) {
    this.loginForm = this.fb.group({
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required, Validators.minLength(6)]],
    });
  }

  ngOnInit(): void {}

  onSubmit(): void {
    if (this.loginForm.invalid) {
      this.loginForm.markAllAsTouched();
      return;
    }

    this.isLoading = true;
    this.error = null;
    const { email, password } = this.loginForm.value;

    // Simulate API call
    console.log('Login attempt:', { email, password });
    setTimeout(() => {
      this.isLoading = false;
      if (email === 'test@example.com' && password === 'password') { // Dummy check
        alert('Login successful!');
        this.router.navigate(['/dashboard']);
      } else {
        this.error = 'Invalid credentials (dummy check failed).';
      }
    }, 1500);

    // Uncomment and use this when integrating with actual API
    // this.apiService.login({ email, password }).subscribe({
    //   next: () => {
    //     this.isLoading = false;
    //     this.router.navigate(['/dashboard']);
    //   },
    //   error: (err) => {
    //     this.isLoading = false;
    //     this.error = err.error?.detail || 'Login failed. Please check your credentials.';
    //   }
    // });
  }
}
