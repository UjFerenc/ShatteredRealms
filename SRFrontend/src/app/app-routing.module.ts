import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { LoreComponent } from './lore/lore.component';

const routes: Routes = [
  {path: "", component: HomeComponent},
  {path: "lore", component: LoreComponent},
  {path: "user", loadChildren:() => import('./user/user.module').then(m => m.UserModule)}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
