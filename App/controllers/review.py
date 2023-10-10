from App.models import Reviews
from App.models import Student
from App.models import User 
from App.database import db


# Creates a review
def create_review(user_id, student_id, review_text):
    user = User.query.get(user.id)
    student = Student.query.get(student_id)

    if user and student:
        review = Review(user_id, student_id, review_text)
        
        db.session.add(review)
        db.session.commit()

        user.reviews.append(review)
        student.reviews.append.append(review)

        db.session.add(user)
        db.session.add(student)
        db.session.commit()

        return review

# Upvotes a review
def upvote_review(review_id, user_id):
    review = Review.query.get(review_id)
    user = User.query.get(user.id)

    if review and user:
        review.vote(user_id, "+1")
        
        db.session.add(review)
        db.session.commit()
        
        return review


# Downvotes a review
def downvote_review(review_id, user_id):
    review = Review.query.get(review_id)
    user = User.query.get(user.id)

    if review and user:
        review.vote(user_id, "-1")
        
        db.session.add(review)
        db.session.commit()
        
        return review