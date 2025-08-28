import { Routes } from '@angular/router';

import { DashboardComponent } from './pages/dashboard/dashboard';
import { UploadComponent } from './pages/upload/upload';
import { QuizzesComponent } from './pages/quizzes/quizzes';
import { FlashcardsComponent } from './pages/flashcards/flashcards';
import { TutorComponent } from './pages/tutor/tutor';
import { SettingsComponent } from './pages/settings/settings';
import { Login } from './login/login';
import { Register } from './register/register';
import { MainLayoutComponent } from './main-layout/main-layout';  

export const routes: Routes = [
  { path: '', redirectTo: 'login', pathMatch: 'full' },

  // Public (no navbar)
  { path: 'login', component: Login },
  { path: 'register', component: Register },

  // Protected (with navbar inside MainLayoutComponent)
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

  // Fallback
  { path: '**', redirectTo: 'login' }
];
