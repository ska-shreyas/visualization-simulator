import { TestBed } from '@angular/core/testing';

import { ManualMsgService } from './manual-msg.service';

describe('ManualMsgService', () => {
  let service: ManualMsgService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ManualMsgService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
