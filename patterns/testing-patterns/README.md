# Testing Patterns for AI-Assisted Development

**Purpose**: Proven testing strategies and workflows for AI coding assistants.

**Value**: Comprehensive test coverage, zero production pollution, efficient testing, high-quality code.

---

## Philosophy

**Good testing practices**:
- Write tests with implementation (not after)
- Test behavior, not implementation
- Isolate tests (no shared state)
- Use mocks for external dependencies
- Maintain test environments separately from production
- Run tests frequently

**Bad testing practices**:
- Write tests after code is "done"
- Test implementation details
- Share state between tests
- Use real external services in tests
- Mix test and production data
- Only run tests before release

---

## Core Testing Patterns

### Pattern: AI-Assisted Test Generation

**Problem**: Writing comprehensive tests is time-consuming.

**Solution**: AI generates test cases based on code analysis.

```python
# AI analyzes this function
def process_refund(payment_id: str, amount: int) -> Refund:
    payment = Payment.query.get(payment_id)
    if not payment:
        raise PaymentNotFound(payment_id)
    if amount > payment.amount:
        raise InvalidRefundAmount("Refund exceeds payment")
    if payment.status != PaymentStatus.COMPLETED:
        raise CannotRefund("Payment not completed")

    return Refund.create(payment_id=payment_id, amount=amount)

# AI generates comprehensive tests
class TestProcessRefund:
    def test_successful_refund(self):
        """Test refund with valid payment and amount"""
        payment = PaymentFactory(amount=10000, status=PaymentStatus.COMPLETED)
        refund = process_refund(payment.id, 5000)
        assert refund.amount == 5000

    def test_payment_not_found(self):
        """Test refund with non-existent payment"""
        with pytest.raises(PaymentNotFound):
            process_refund("invalid_id", 5000)

    def test_refund_exceeds_payment(self):
        """Test refund amount greater than payment"""
        payment = PaymentFactory(amount=10000)
        with pytest.raises(InvalidRefundAmount):
            process_refund(payment.id, 15000)

    def test_payment_not_completed(self):
        """Test refund on non-completed payment"""
        payment = PaymentFactory(status=PaymentStatus.PENDING)
        with pytest.raises(CannotRefund):
            process_refund(payment.id, 5000)

    def test_full_refund(self):
        """Test full refund equals payment amount"""
        payment = PaymentFactory(amount=10000)
        refund = process_refund(payment.id, 10000)
        assert refund.amount == 10000
```

**AI Test Generation Process**:
1. Analyze function signature and body
2. Identify happy path
3. Identify error conditions
4. Identify edge cases
5. Generate test for each scenario
6. Add descriptive docstrings

---

### Pattern: Test-Driven Development with AI

**Problem**: Traditional TDD is slow; AI can accelerate it.

**Solution**: AI writes failing tests first, then implements to pass them.

```markdown
TDD Workflow with AI:

1. Write Failing Test (AI)
   "Create test for email verification feature"
   AI writes: test_verify_email_with_valid_token()
   Status: RED (no implementation)

2. Implement Minimal Code (AI)
   "Implement just enough to pass the test"
   AI implements: verify_email() method
   Status: GREEN (test passes)

3. Refactor (AI + Human)
   "Improve implementation while keeping tests green"
   AI suggests refactoring
   Status: GREEN (tests still pass)

4. Repeat
   Add next test, implement, refactor
```

**Benefits**:
- Tests define requirements clearly
- No untested code
- Refactoring confidence
- AI ensures tests are comprehensive

---

### Pattern: Mock External Dependencies

**Problem**: Tests should not depend on external services (databases, APIs, etc.).

**Solution**: Mock all external dependencies.

```python
# BAD (tests depend on real database)
def test_get_user():
    user = User.query.get(1)  # Real database query
    assert user.email == "test@example.com"

# GOOD (mock database)
def test_get_user(mock_db):
    mock_user = Mock(id=1, email="test@example.com")
    mock_db.query.return_value.get.return_value = mock_user

    user = User.query.get(1)
    assert user.email == "test@example.com"
```

**What to Mock**:
- ✅ Databases (use in-memory or mocks)
- ✅ External APIs (Stripe, SendGrid, etc.)
- ✅ File system operations
- ✅ Network requests
- ✅ Time/dates (for consistency)

**What NOT to Mock**:
- ❌ Code you're testing
- ❌ Standard library (unless time/random)
- ❌ Simple data structures

---

### Pattern: Test Fixtures and Factories

**Problem**: Creating test data is repetitive.

**Solution**: Use fixtures and factories for test data.

```python
# Using pytest fixtures
@pytest.fixture
def sample_user():
    return User(
        id=1,
        email="test@example.com",
        name="Test User",
        email_verified=True
    )

def test_user_profile(sample_user):
    profile = UserProfile(sample_user)
    assert profile.display_name == "Test User"

# Using factory pattern (Factory Boy)
class UserFactory(factory.Factory):
    class Meta:
        model = User

    id = factory.Sequence(lambda n: n)
    email = factory.Faker('email')
    name = factory.Faker('name')
    email_verified = True

def test_user_creation():
    user = UserFactory()  # Creates user with generated data
    assert user.email_verified is True
```

**Benefits**:
- Consistent test data
- Less repetitive code
- Easy to create variations
- Readable tests

---

### Pattern: Test Isolation and Cleanup

**Problem**: Tests affecting each other causes flaky tests.

**Solution**: Ensure complete isolation between tests.

```python
# Use pytest fixtures for setup/teardown
@pytest.fixture(autouse=True)
def setup_teardown():
    # Setup: Create clean test database
    db.create_all()
    yield
    # Teardown: Clean up after test
    db.session.remove()
    db.drop_all()

# Or use database transactions
@pytest.fixture
def db_session():
    connection = db.engine.connect()
    transaction = connection.begin()
    session = db.session(bind=connection)

    yield session

    transaction.rollback()
    connection.close()
```

**Isolation Rules**:
- Each test starts with clean state
- No shared global variables
- No database state persists between tests
- Tests can run in any order
- Tests can run in parallel

---

### Pattern: Testing AI-Generated Code

**Problem**: AI-generated code needs validation through tests.

**Solution**: AI writes tests alongside implementation.

```markdown
AI Workflow:

1. User: "Add email verification feature"

2. AI Implements Feature
   - Create User.verify_email() method
   - Add verification endpoint
   - Update database model

3. AI Writes Tests (automatically)
   - Unit tests for User.verify_email()
   - Integration tests for API endpoint
   - Edge case tests (invalid token, expired token)

4. AI Runs Tests
   pytest tests/test_user.py -v

5. AI Reports
   "✅ All 8 tests passing
    - test_verify_email_success
    - test_verify_email_invalid_token
    - test_verify_email_expired_token
    - ..."

6. User Reviews
   - Code looks good
   - Tests cover edge cases
   - Merge PR
```

**AI Testing Checklist**:
- [ ] Unit tests for each method
- [ ] Integration tests for APIs
- [ ] Edge cases covered
- [ ] Error conditions tested
- [ ] All tests passing

---

### Pattern: Coverage-Driven Testing

**Problem**: Don't know which code lacks tests.

**Solution**: Use coverage reports to guide test creation.

```bash
# Run tests with coverage
pytest --cov=src --cov-report=html

# AI analyzes coverage report
AI: "Coverage analysis shows:
     - src/services/payment.py: 85% coverage
     - Missing coverage: lines 145-160 (refund edge cases)

     Shall I add tests for the uncovered lines?"

User: "Yes, please"

# AI creates targeted tests
class TestPaymentServiceCoverage:
    def test_refund_partial_amount(self):
        """Test partial refund (covers line 148)"""
        ...

    def test_refund_zero_amount(self):
        """Test refund with zero amount (covers line 152)"""
        ...
```

**Coverage Goals**:
- **Critical code**: 100% (payment, auth, security)
- **Business logic**: 90%+
- **Integration code**: 80%+
- **UI code**: 60-70%

---

### Pattern: Integration Test Patterns

**Problem**: Unit tests pass but system doesn't work together.

**Solution**: Write integration tests for critical paths.

```python
# Integration test example
def test_user_registration_flow():
    """Test complete user registration flow"""
    # 1. User submits registration
    response = client.post('/api/auth/register', json={
        'email': 'new@example.com',
        'password': 'secure_pass_123'
    })
    assert response.status_code == 201

    # 2. Verification email sent
    assert len(mail.outbox) == 1
    assert 'verify' in mail.outbox[0].subject

    # 3. Extract verification token from email
    token = extract_token_from_email(mail.outbox[0])

    # 4. Verify email with token
    response = client.post('/api/auth/verify', json={'token': token})
    assert response.status_code == 200

    # 5. User can now log in
    response = client.post('/api/auth/login', json={
        'email': 'new@example.com',
        'password': 'secure_pass_123'
    })
    assert response.status_code == 200
    assert 'access_token' in response.json
```

**Integration Test Targets**:
- User workflows (registration, login, purchase)
- API endpoint chains
- Database + Service + API layers
- External service integrations (with mocks)

---

## Best Practices

### Do
- ✅ Write tests alongside implementation
- ✅ Mock external dependencies
- ✅ Isolate tests completely
- ✅ Use descriptive test names
- ✅ Test edge cases and errors
- ✅ Run tests frequently
- ✅ Aim for high coverage on critical code

### Don't
- ❌ Write tests after code is "done"
- ❌ Use real external services in tests
- ❌ Share state between tests
- ❌ Skip edge case testing
- ❌ Commit failing tests
- ❌ Test implementation details
- ❌ Mix test and production data

---

## Quick Reference

### Test Structure (AAA Pattern)
```python
def test_feature():
    # Arrange: Set up test data
    user = UserFactory()

    # Act: Perform action
    result = user.verify_email(token)

    # Assert: Verify outcome
    assert result is True
    assert user.email_verified is True
```

### Running Tests
```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_user.py

# Run with coverage
pytest --cov=src --cov-report=html

# Run tests matching pattern
pytest -k "email_verification"

# Run in parallel
pytest -n auto
```

### Test Naming Convention
```python
# Pattern: test_<what>_<condition>_<expected>
def test_verify_email_with_valid_token_returns_true()
def test_verify_email_with_invalid_token_raises_error()
def test_verify_email_with_expired_token_returns_false()
```

---

## Real-World Success: The Symposium

**Project**: Distributed AI consciousness platform
**Testing Achievement**: 81 tests, 100% pass rate, zero production pollution

**Key Patterns Used**:
1. **Mock External Services**: OpenSearch, Redis mocked in tests
2. **Test Isolation**: Each test with clean database state
3. **Comprehensive Coverage**: All critical paths tested
4. **AI-Generated Tests**: AI wrote majority of tests alongside code
5. **Integration Tests**: Full workflow tests for critical features

**Results**:
- ✅ 81 tests created (50+ by AI)
- ✅ 100% pass rate maintained
- ✅ Zero production data pollution
- ✅ Confident refactoring enabled
- ✅ Bugs caught before deployment

---

## Related Patterns

- [Error Recovery](../error-recovery/README.md) - Testing error handling
- [Tool Use](../tool-use/README.md) - Efficient test execution
- [Git Workflows](../git-workflows/README.md) - Committing tests with code

---

## Related Core Rules

**See Also**:
- [Testing Standards](../../core-rules/testing/) - Testing requirements and standards
- [Pytest Standards](../../core-rules/testing/UNIT_TESTING.md) - Pytest-specific guidelines

**Note**: This patterns directory focuses on **HOW** to test effectively (workflows, strategies, examples). The core-rules directory defines **WHAT** is required (standards, coverage thresholds, tooling requirements).

---

**Last Updated**: 2025-12-29
**Source**: The Symposium development (v0.4.5) - 81 tests, 100% pass rate
**Status**: Complete
**Real-World Validation**: ✅ Battle-tested in production

*"Test early, test often, test confidently - AI makes it faster, not optional."*
