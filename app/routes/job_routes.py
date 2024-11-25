from flask import Blueprint, request, jsonify
from app.models.job import Job
from app import db

bp = Blueprint('jobs', __name__)

@bp.route('/', methods=['GET'])
def get_jobs():
    jobs = Job.query.all()
    return jsonify([job.to_dict() for job in jobs])

@bp.route('/', methods=['POST'])
def create_job():
    data = request.get_json()
    
    new_job = Job(title=data['title'], company=data['company'], location=data['location'], link=data['link'])
    
    db.session.add(new_job)
    db.session.commit()

    return jsonify({"message": "Job created successfully!"}), 201

@bp.route('/<int:job_id>', methods=['DELETE'])
def delete_job(job_id):
    job = Job.query.get(job_id)

    if not job:
        return jsonify({"error": "Job not found"}), 404
    
    db.session.delete(job)
    db.session.commit()

    return jsonify({"message": f"Job {job_id} deleted successfully!"})