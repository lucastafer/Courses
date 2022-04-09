import { Formik, useField } from 'formik';
import React from 'react';
import * as yup from 'yup';

const Field = ({ label, ...props }) => {
  const [field, meta] = useField(props);
  return (
    <div className="form-group">
      <label htmlFor={props.id}>{label}</label>
      <input
        {...field}
        {...props}
        className={meta.error && meta.touched ? 'is-invalid' : ''}
      />
      {meta.error && meta.touched ? (
        <div className="invalid-feedback">{meta.error}</div>
      ) : null}
    </div>
  );
};

export default function AddClient () {
  const schema = yup.object({
    name: yup
      .string()
      .required('Name is required.')
      .min(10, 'Name must have at least 10 characters.')
      .max(30, 'Name must be a maximum of 30 characters.'),
    email: yup
      .string()
      .required('Email is required.')
      .email('Email is invalid.'),
    birth: yup
      .date()
      .required('Birth date is required.')
      .max(new Date(), `You can't have borned in future...`),
  });

  return (
    <>
      <h1>Client Register Menu</h1>

      <Formik
        initialValues={{ name: '', email: '', birth: '' }}
        validationSchema={schema}
        onSubmit={(values) => {
          alert(JSON.stringify(values));
        }}
      >
        {(props) => (
          <form onSubmit={props.handleSubmit} noValidate>
            <Field type="text" id="name" name="name" label="Name" />
            <Field type="email" id="email" name="email" label="Email" />
            <Field
              type="date"
              id="birth"
              name="birth"
              label="Birth date"
            />
            <button type="submit">Register</button>
          </form>
        )}
      </Formik>
    </>
  );
};
