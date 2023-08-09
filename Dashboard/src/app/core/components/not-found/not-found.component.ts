import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-not-found',
  templateUrl: './not-found.component.html',
  styleUrls: ['./not-found.component.scss']
})
export class NotFoundComponent implements OnInit {

  tema: string = '';

  url: string;
  constructor(private router: Router,private routeAct: ActivatedRoute) {
    this.url = this.routeAct.snapshot.params['url'];
  }

  ngOnInit()
  {
    this.tema = localStorage['tema'];
  }

  redireccionar()
  {
    this.router.navigate(["/home"]);
  }
}
