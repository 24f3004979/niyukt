-- Application Checkout trigger

CREATE TRIGGER deadline_check
BEFORE INSERT ON application 
FOR EACH ROW
  BEGIN
    SELECT CASE 
      WHEN ( SELECT deadline FROM placement_drive WHERE id = NEW.drive_id ) < CURRENT_TIMESTAMP
      THEN RAISE(ABORT , 'DEADLINE PASSED :)')
  END;
END;


-- Application Checkout update : triggers with applications status update
CREATE TRIGGER application_checkout
AFTER UPDATE OF status ON application 
FOR EACH ROW
  WHEN NEW.status IN ('selected', 'rejected')
  BEGIN
    INSERT OR IGNORE INTO placement_history (
      student_id,
      drive_id,
      final_result
    )
    VALUES(
      NEW.student_id,
      NEW.drive_id,
      NEW.status
    );
  END;

-- Final Check for restriction of NO going back with selected students
CREATE TRIGGER prevent_invalid_transition
BEFORE UPDATE OF status ON application
  FOR EACH ROW
WHEN OLD.status IN ('selected', 'rejected')
BEGIN
    SELECT RAISE(ABORT, 'Finalized applications cannot be modified');
END;


