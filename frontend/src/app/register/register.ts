import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { Router, RouterModule } from '@angular/router';
import { HttpClientModule } from '@angular/common/http'; // <--- ADD THIS IMPORT
import { ApiService } from '../services/api';

@Component({
  selector: 'app-register',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule, RouterModule, HttpClientModule], // <--- ADD HttpClientModule here
  templateUrl: './register.html',
  styleUrls: ['./register.css']
})
export class Register implements OnInit {
  registerForm: FormGroup;
  isLoading = false;
  error: string | null = null;

  constructor(
    private fb: FormBuilder,
    private apiService: ApiService,
    private router: Router
  ) {
    this.registerForm = this.fb.group({
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required, Validators.minLength(6)]],
    });
  }

  ngOnInit(): void {}

  onSubmit(): void {
    if (this.registerForm.invalid) {
      this.registerForm.markAllAsTouched();
      return;
    }

    this.isLoading = true;
    this.error = null;
    const { email, password } = this.registerForm.value;

    // Simulate API call
    console.log('Register attempt:', { email, password });
    setTimeout(() => {
      this.isLoading = false;
      alert('Registration successful! Please log in.');
      this.router.navigate(['/login']);
    }, 1500);

    // Uncomment and use this when integrating with actual API
    // this.apiService.register({ email, password }).subscribe({
    //   next: () => {
    //     this.isLoading = false;
    //     this.router.navigate(['/login']); // Redirect to login after successful registration
    //   },
    //   error: (err) => {
    //     this.isLoading = false;
    //     this.error = err.error?.detail || 'Registration failed. Please try again.';
    //   }
    // });
  }
}
