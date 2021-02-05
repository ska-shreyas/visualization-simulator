import { TestBed } from '@angular/core/testing';

import { AutoMsgService } from './auto-msg.service';

describe('AutoMsgService', () => {
  let service: AutoMsgService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(AutoMsgService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
