import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { CommonModule } from '@angular/common';
import { ReactiveFormsModule, FormBuilder, FormGroup, Validators } from '@angular/forms';
import { HttpClient, HttpErrorResponse, HttpClientModule } from '@angular/common/http';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-register',
  standalone: true,
  imports: [
    CommonModule,
    ReactiveFormsModule,
    RouterModule,
    HttpClientModule
  ],
  templateUrl: './register.html',
  styleUrls: ['./register.css']
})
export class Register implements OnInit {
  registerForm!: FormGroup;
  errorMessage: string | null = null;
  successMessage: string | null = null;
  isLoading = false;

  constructor(private fb: FormBuilder, private http: HttpClient, private router: Router) {}

  ngOnInit(): void {
    this.registerForm = this.fb.group({
      fullname: ['', [Validators.required, Validators.minLength(3)]],
      username: ['', [Validators.required, Validators.minLength(3)]],
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required, Validators.minLength(6)]]
    });
  }

  onSubmit() {
    if (this.registerForm.invalid) {
      this.registerForm.markAllAsTouched();
      return;
    }

    this.isLoading = true;
    this.errorMessage = null;
    this.successMessage = null;

    const {fullname ,username, email, password } = this.registerForm.value;

    this.http.post('http://127.0.0.1:8000/api/auth/register', { fullname, username, email, password })
      .subscribe({
        next: (response: any) => {
          if (response.message === "User registered successfully.") {
            this.successMessage = 'Registration successful! You can now log in.';
            this.registerForm.reset();
            setTimeout(() => {
              this.router.navigate(['/login']);
            }, 8000);
          } else {
            this.errorMessage = 'Registration failed. Please try again.';
          }
          this.isLoading = false;
        },
        error: (error: HttpErrorResponse) => {
          if (error.status === 409) {
            this.errorMessage = 'Email is already registered. Please use a different email or log in.';
          } else {
            this.errorMessage = 'An unexpected error occurred. Please try again later.';
          }
          this.isLoading = false;
        }
      });
  }
}
