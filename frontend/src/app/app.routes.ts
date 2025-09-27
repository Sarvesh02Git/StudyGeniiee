// src/app/app.routes.ts
import { Routes } from '@angular/router';

import { Auth } from './auth/auth';
import { MainLayoutComponent } from './main-layout/main-layout';
import { DashboardComponent } from './pages/dashboard/dashboard';
import { UploadComponent } from './pages/upload/upload';
import { QuizzesComponent } from './pages/quizzes/quizzes';
import { FlashcardsComponent } from './pages/flashcards/flashcards';
import { TutorComponent } from './pages/tutor/tutor';
import { SettingsComponent } from './pages/settings/settings';
import { Login } from './login/login';
import { Register } from './register/register';
import { ForgotPassword } from './forgot-password/forgot-password';
import { ResetPassword } from './reset-password/reset-password';

export const routes: Routes = [
  // Public routes (without a navbar)
  { path: '', redirectTo: 'login', pathMatch: 'full' },
  { path: 'login', component: Login },
  { path: 'register', component: Register },
  { path: 'forgot-password', component: ForgotPassword },
  { path: 'reset-password', component: ResetPassword }, 

  // Protected routes (with the navbar from MainLayoutComponent)
  {
    path: '',
    component: MainLayoutComponent,
    children: [
      { path: 'dashboard', component: DashboardComponent },
      { path: 'upload', component: UploadComponent },
      { path: 'quizzes', component: QuizzesComponent },
      { path: 'flashcards', component: FlashcardsComponent },
      { path: 'tutor', component: TutorComponent },
      { path: 'settings', component: SettingsComponent },
    ]
  },

  // Fallback route for 404
  { path: '**', redirectTo: 'login' }
];
